from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///boardroom.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)

# Database Models
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='scheduled')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    agenda_items = db.relationship('AgendaItem', backref='meeting', lazy=True, cascade='all, delete-orphan')
    minutes = db.relationship('MeetingMinutes', backref='meeting', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date.isoformat(),
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class AgendaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    order = db.Column(db.Integer, default=0)
    duration_minutes = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'meeting_id': self.meeting_id,
            'title': self.title,
            'description': self.description,
            'order': self.order,
            'duration_minutes': self.duration_minutes
        }

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    document_type = db.Column(db.String(50))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    summary = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content[:200] + '...' if len(self.content) > 200 else self.content,
            'document_type': self.document_type,
            'uploaded_at': self.uploaded_at.isoformat(),
            'summary': self.summary
        }

class MeetingMinutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    action_items = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'meeting_id': self.meeting_id,
            'content': self.content,
            'summary': self.summary,
            'action_items': self.action_items,
            'created_at': self.created_at.isoformat()
        }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api_info():
    return jsonify({
        'message': 'Welcome to AI Boardroom API',
        'version': '1.0.0',
        'endpoints': {
            'meetings': '/api/meetings',
            'documents': '/api/documents',
            'agenda': '/api/agenda',
            'minutes': '/api/minutes'
        }
    })

# Meeting endpoints
@app.route('/api/meetings', methods=['GET', 'POST'])
def meetings():
    if request.method == 'GET':
        meetings = Meeting.query.order_by(Meeting.date.desc()).all()
        return jsonify([m.to_dict() for m in meetings])
    
    elif request.method == 'POST':
        data = request.json
        meeting = Meeting(
            title=data['title'],
            description=data.get('description', ''),
            date=datetime.fromisoformat(data['date']),
            status=data.get('status', 'scheduled')
        )
        db.session.add(meeting)
        db.session.commit()
        return jsonify(meeting.to_dict()), 201

@app.route('/api/meetings/<int:meeting_id>', methods=['GET', 'PUT', 'DELETE'])
def meeting_detail(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    
    if request.method == 'GET':
        result = meeting.to_dict()
        result['agenda_items'] = [item.to_dict() for item in meeting.agenda_items]
        result['minutes'] = [m.to_dict() for m in meeting.minutes]
        return jsonify(result)
    
    elif request.method == 'PUT':
        data = request.json
        meeting.title = data.get('title', meeting.title)
        meeting.description = data.get('description', meeting.description)
        if 'date' in data:
            meeting.date = datetime.fromisoformat(data['date'])
        meeting.status = data.get('status', meeting.status)
        db.session.commit()
        return jsonify(meeting.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(meeting)
        db.session.commit()
        return '', 204

# Agenda Item endpoints
@app.route('/api/meetings/<int:meeting_id>/agenda', methods=['GET', 'POST'])
def agenda_items(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    
    if request.method == 'GET':
        items = AgendaItem.query.filter_by(meeting_id=meeting_id).order_by(AgendaItem.order).all()
        return jsonify([item.to_dict() for item in items])
    
    elif request.method == 'POST':
        data = request.json
        item = AgendaItem(
            meeting_id=meeting_id,
            title=data['title'],
            description=data.get('description', ''),
            order=data.get('order', 0),
            duration_minutes=data.get('duration_minutes')
        )
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201

@app.route('/api/agenda/<int:item_id>', methods=['PUT', 'DELETE'])
def agenda_item_detail(item_id):
    item = AgendaItem.query.get_or_404(item_id)
    
    if request.method == 'PUT':
        data = request.json
        item.title = data.get('title', item.title)
        item.description = data.get('description', item.description)
        item.order = data.get('order', item.order)
        item.duration_minutes = data.get('duration_minutes', item.duration_minutes)
        db.session.commit()
        return jsonify(item.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 204

# Document endpoints
@app.route('/api/documents', methods=['GET', 'POST'])
def documents():
    if request.method == 'GET':
        docs = Document.query.order_by(Document.uploaded_at.desc()).all()
        return jsonify([d.to_dict() for d in docs])
    
    elif request.method == 'POST':
        data = request.json
        doc = Document(
            title=data['title'],
            content=data.get('content', ''),
            document_type=data.get('document_type', 'general'),
            summary=data.get('summary', '')
        )
        db.session.add(doc)
        db.session.commit()
        return jsonify(doc.to_dict()), 201

@app.route('/api/documents/<int:doc_id>', methods=['GET', 'PUT', 'DELETE'])
def document_detail(doc_id):
    doc = Document.query.get_or_404(doc_id)
    
    if request.method == 'GET':
        result = doc.to_dict()
        result['content'] = doc.content  # Full content for detail view
        return jsonify(result)
    
    elif request.method == 'PUT':
        data = request.json
        doc.title = data.get('title', doc.title)
        doc.content = data.get('content', doc.content)
        doc.document_type = data.get('document_type', doc.document_type)
        doc.summary = data.get('summary', doc.summary)
        db.session.commit()
        return jsonify(doc.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(doc)
        db.session.commit()
        return '', 204

# Meeting Minutes endpoints
@app.route('/api/meetings/<int:meeting_id>/minutes', methods=['GET', 'POST'])
def meeting_minutes(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    
    if request.method == 'GET':
        minutes = MeetingMinutes.query.filter_by(meeting_id=meeting_id).all()
        return jsonify([m.to_dict() for m in minutes])
    
    elif request.method == 'POST':
        data = request.json
        minutes = MeetingMinutes(
            meeting_id=meeting_id,
            content=data['content'],
            summary=data.get('summary', ''),
            action_items=data.get('action_items', '')
        )
        db.session.add(minutes)
        db.session.commit()
        return jsonify(minutes.to_dict()), 201

@app.route('/api/minutes/<int:minutes_id>', methods=['GET', 'PUT', 'DELETE'])
def minutes_detail(minutes_id):
    minutes = MeetingMinutes.query.get_or_404(minutes_id)
    
    if request.method == 'GET':
        return jsonify(minutes.to_dict())
    
    elif request.method == 'PUT':
        data = request.json
        minutes.content = data.get('content', minutes.content)
        minutes.summary = data.get('summary', minutes.summary)
        minutes.action_items = data.get('action_items', minutes.action_items)
        db.session.commit()
        return jsonify(minutes.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(minutes)
        db.session.commit()
        return '', 204

# AI-powered summarization endpoint
@app.route('/api/summarize', methods=['POST'])
def summarize_content():
    """Generate AI summary of content (placeholder - requires OpenAI API key)"""
    data = request.json
    content = data.get('content', '')
    
    # Simple summarization logic (can be replaced with OpenAI API)
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    # Placeholder summary - in production, use OpenAI API
    words = content.split()
    summary = ' '.join(words[:50]) + '...' if len(words) > 50 else content
    
    return jsonify({
        'summary': summary,
        'action_items': 'AI-generated action items would appear here',
        'key_points': ['Key point 1', 'Key point 2', 'Key point 3']
    })

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Only enable debug mode in development
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
