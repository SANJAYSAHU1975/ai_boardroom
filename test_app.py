import unittest
import json
from app import app, db, Meeting, Document, AgendaItem, MeetingMinutes
from datetime import datetime

class AIBoardroomTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and initialize test database"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        """Clean up after tests"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_home_page(self):
        """Test that home page loads"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_api_info(self):
        """Test API info endpoint"""
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('version', data)
        self.assertIn('endpoints', data)
    
    def test_create_meeting(self):
        """Test creating a new meeting"""
        meeting_data = {
            'title': 'Test Board Meeting',
            'description': 'Test meeting description',
            'date': '2025-12-31T10:00:00',
            'status': 'scheduled'
        }
        response = self.app.post(
            '/api/meetings',
            data=json.dumps(meeting_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Board Meeting')
        self.assertEqual(data['status'], 'scheduled')
    
    def test_get_meetings(self):
        """Test retrieving meetings list"""
        response = self.app.get('/api/meetings')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
    
    def test_get_meeting_detail(self):
        """Test getting a specific meeting"""
        # First create a meeting
        with app.app_context():
            meeting = Meeting(
                title='Test Meeting',
                description='Test description',
                date=datetime(2025, 12, 31, 10, 0)
            )
            db.session.add(meeting)
            db.session.commit()
            meeting_id = meeting.id
        
        # Now retrieve it
        response = self.app.get(f'/api/meetings/{meeting_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Meeting')
    
    def test_update_meeting(self):
        """Test updating a meeting"""
        # Create a meeting
        with app.app_context():
            meeting = Meeting(
                title='Original Title',
                description='Original description',
                date=datetime(2025, 12, 31, 10, 0)
            )
            db.session.add(meeting)
            db.session.commit()
            meeting_id = meeting.id
        
        # Update it
        update_data = {
            'title': 'Updated Title',
            'status': 'completed'
        }
        response = self.app.put(
            f'/api/meetings/{meeting_id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Title')
        self.assertEqual(data['status'], 'completed')
    
    def test_delete_meeting(self):
        """Test deleting a meeting"""
        # Create a meeting
        with app.app_context():
            meeting = Meeting(
                title='To Be Deleted',
                description='Test',
                date=datetime(2025, 12, 31, 10, 0)
            )
            db.session.add(meeting)
            db.session.commit()
            meeting_id = meeting.id
        
        # Delete it
        response = self.app.delete(f'/api/meetings/{meeting_id}')
        self.assertEqual(response.status_code, 204)
        
        # Verify it's gone
        response = self.app.get(f'/api/meetings/{meeting_id}')
        self.assertEqual(response.status_code, 404)
    
    def test_create_document(self):
        """Test creating a document"""
        doc_data = {
            'title': 'Test Document',
            'content': 'This is test content',
            'document_type': 'general',
            'summary': 'Test summary'
        }
        response = self.app.post(
            '/api/documents',
            data=json.dumps(doc_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Document')
    
    def test_get_documents(self):
        """Test retrieving documents list"""
        response = self.app.get('/api/documents')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
    
    def test_create_agenda_item(self):
        """Test creating an agenda item"""
        # First create a meeting
        with app.app_context():
            meeting = Meeting(
                title='Test Meeting',
                description='Test',
                date=datetime(2025, 12, 31, 10, 0)
            )
            db.session.add(meeting)
            db.session.commit()
            meeting_id = meeting.id
        
        # Create agenda item
        agenda_data = {
            'title': 'Budget Review',
            'description': 'Review Q4 budget',
            'order': 1,
            'duration_minutes': 30
        }
        response = self.app.post(
            f'/api/meetings/{meeting_id}/agenda',
            data=json.dumps(agenda_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Budget Review')
    
    def test_create_meeting_minutes(self):
        """Test creating meeting minutes"""
        # First create a meeting
        with app.app_context():
            meeting = Meeting(
                title='Test Meeting',
                description='Test',
                date=datetime(2025, 12, 31, 10, 0)
            )
            db.session.add(meeting)
            db.session.commit()
            meeting_id = meeting.id
        
        # Create minutes
        minutes_data = {
            'content': 'Full meeting transcript',
            'summary': 'Meeting summary',
            'action_items': 'Action item 1\nAction item 2'
        }
        response = self.app.post(
            f'/api/meetings/{meeting_id}/minutes',
            data=json.dumps(minutes_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['content'], 'Full meeting transcript')
    
    def test_summarize_content(self):
        """Test content summarization endpoint"""
        content_data = {
            'content': 'This is a long piece of content that needs to be summarized. ' * 10
        }
        response = self.app.post(
            '/api/summarize',
            data=json.dumps(content_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('summary', data)
        self.assertIn('action_items', data)
        self.assertIn('key_points', data)
    
    def test_summarize_empty_content(self):
        """Test summarization with empty content"""
        response = self.app.post(
            '/api/summarize',
            data=json.dumps({'content': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
