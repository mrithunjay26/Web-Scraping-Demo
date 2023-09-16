from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb+srv://mrithunjay26:77820897@comments.jx9xmpc.mongodb.net/Comments'
mongo = PyMongo(app)

# Define the MongoDB collection for comments
comments_collection = mongo.db.comments

@app.route('/addComment', methods=['POST'])
def add_comment():
    data = request.get_json()
    if 'text' in data:
        comment = {
            'text': data['text'],
            'likes': 0,
            'dislikes': 0
        }
        inserted_comment = comments_collection.insert_one(comment)
        return jsonify({'success': True, 'comment_id': str(inserted_comment.inserted_id)})
    else:
        return jsonify({'success': False, 'error': 'Invalid data'})

@app.route('/getComments', methods=['GET'])
def get_comments():
    comments = list(comments_collection.find({}, {'_id': False}))
    return jsonify(comments)

@app.route('/likeDislikeComment', methods=['POST'])
def like_dislike_comment():
    data = request.get_json()
    comment_text = data.get('text')  # Get the comment text from the request
    action = data.get('action')

    if action not in ['like', 'dislike']:
        return jsonify({'success': False, 'error': 'Invalid action'})

    # Find the comment by text
    query = {'text': comment_text}
    update_field = 'likes' if action == 'like' else 'dislikes'

    result = comments_collection.update_one(query, {'$inc': {update_field: 1}})

    if result.matched_count > 0:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Comment not found'})

if __name__ == '__main__':
    app.run(debug=True)
