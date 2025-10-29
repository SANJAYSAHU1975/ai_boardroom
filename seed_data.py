"""
Seed the database with sample data for demonstration purposes.
Run this script to populate the database with example meetings, documents, and agenda items.
"""
from app import app, db, Meeting, Document, AgendaItem, MeetingMinutes
from datetime import datetime, timedelta

def seed_database():
    """Populate database with sample data"""
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create sample meetings
        print("Creating sample meetings...")
        meeting1 = Meeting(
            title="Q4 2025 Board Meeting",
            description="Quarterly review of company performance and strategic initiatives",
            date=datetime.now() + timedelta(days=7),
            status="scheduled"
        )
        
        meeting2 = Meeting(
            title="Annual Strategic Planning Session",
            description="Annual strategy review and planning for 2026",
            date=datetime.now() + timedelta(days=30),
            status="scheduled"
        )
        
        meeting3 = Meeting(
            title="Emergency Board Meeting - Budget Review",
            description="Emergency session to review and approve budget adjustments",
            date=datetime.now() - timedelta(days=5),
            status="completed"
        )
        
        db.session.add_all([meeting1, meeting2, meeting3])
        db.session.commit()
        
        # Create agenda items for meeting1
        print("Creating agenda items...")
        agenda1 = AgendaItem(
            meeting_id=meeting1.id,
            title="Financial Performance Review",
            description="Review Q4 financial results and year-end projections",
            order=1,
            duration_minutes=30
        )
        
        agenda2 = AgendaItem(
            meeting_id=meeting1.id,
            title="Strategic Initiatives Update",
            description="Update on key strategic initiatives and progress",
            order=2,
            duration_minutes=45
        )
        
        agenda3 = AgendaItem(
            meeting_id=meeting1.id,
            title="Risk Assessment",
            description="Review of current risks and mitigation strategies",
            order=3,
            duration_minutes=20
        )
        
        db.session.add_all([agenda1, agenda2, agenda3])
        
        # Create sample documents
        print("Creating sample documents...")
        doc1 = Document(
            title="Q3 Financial Report",
            content="Executive Summary: Q3 showed strong performance with revenue growth of 15% YoY...",
            document_type="financial",
            summary="Strong Q3 performance with 15% revenue growth and improved margins"
        )
        
        doc2 = Document(
            title="2026 Strategic Plan",
            content="Strategic Vision: Our goal for 2026 is to expand into new markets while maintaining core business excellence...",
            document_type="strategic",
            summary="Strategic roadmap for 2026 focusing on market expansion and operational excellence"
        )
        
        doc3 = Document(
            title="Board Governance Policy",
            content="This policy outlines the governance framework and responsibilities of the board of directors...",
            document_type="policy",
            summary="Comprehensive governance policy defining board roles, responsibilities, and procedures"
        )
        
        doc4 = Document(
            title="Risk Management Framework",
            content="The risk management framework establishes processes for identifying, assessing, and mitigating organizational risks...",
            document_type="policy",
            summary="Framework for enterprise risk management including assessment and mitigation strategies"
        )
        
        db.session.add_all([doc1, doc2, doc3, doc4])
        
        # Create meeting minutes for completed meeting
        print("Creating meeting minutes...")
        minutes1 = MeetingMinutes(
            meeting_id=meeting3.id,
            content="""
            Meeting called to order at 10:00 AM
            
            Present: All board members
            
            Agenda Items Discussed:
            1. Budget Review for Q4
            2. Emergency expense approvals
            3. Cost reduction initiatives
            
            Decisions Made:
            - Approved emergency budget allocation of $500K
            - Authorized CFO to implement cost reduction plan
            - Scheduled follow-up meeting in 2 weeks
            
            Meeting adjourned at 11:30 AM
            """,
            summary="Emergency budget meeting resulted in approval of $500K allocation and authorization of cost reduction initiatives",
            action_items="""
            1. CFO to implement cost reduction plan by end of month
            2. Department heads to submit revised budgets by next week
            3. Schedule follow-up meeting in 2 weeks
            4. Prepare detailed financial impact analysis
            """
        )
        
        db.session.add(minutes1)
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   - {Meeting.query.count()} meetings")
        print(f"   - {AgendaItem.query.count()} agenda items")
        print(f"   - {Document.query.count()} documents")
        print(f"   - {MeetingMinutes.query.count()} meeting minutes")

if __name__ == "__main__":
    seed_database()
