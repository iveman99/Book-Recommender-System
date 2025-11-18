from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# ---------------------------------------
# LOAD ALL PKL FILES
# ---------------------------------------
try:
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
    print("✅ PKL files loaded successfully")
except Exception as e:
    print("\n❌ ERROR LOADING PICKLE FILES")
    print("Reason:", e)
    print("👉 FIX: Your PKL files might be version incompatible.\n")


# ---------------------------------------
# HOME PAGE (Top Books)
# ---------------------------------------
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['Number_of_Ratings'].values),
        rating=list(popular_df['Average_Ratings'].values)
    )


# ---------------------------------------
# RECOMMEND PAGE (Search UI)
# ---------------------------------------
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


# ---------------------------------------
# ABOUT PAGE
# ---------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# ---------------------------------------
# RECOMMENDATION LOGIC
# ---------------------------------------
@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')

    # If book is not in index
    if user_input not in pt.index:
        return render_template(
            'recommend.html',
            error="❌ Book not found. Please enter an exact book name."
        )

    # Find index of the selected book
    index = np.where(pt.index == user_input)[0][0]

    # Fetch top 4 similar books
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

        title = temp_df['Book-Title'].values[0]
        author = temp_df['Book-Author'].values[0]
        image = temp_df['Image-URL-M'].values[0]

        data.append([title, author, image])

    return render_template('recommend.html', data=data, user_input=user_input)


# ---------------------------------------
# RUN FLASK SERVER
# ---------------------------------------
if __name__ == '__main__':
    print("🔥 Flask server starting...")
    app.run(debug=True)
