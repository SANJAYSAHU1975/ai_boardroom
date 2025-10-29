#!/usr/bin/env python3
"""
Simple tests for the AI Boardroom system.

These tests verify the basic functionality of the Agent and Boardroom classes.
"""

from agent_bhai import Agent, Boardroom, what_will_you_do_agent_bhai


def test_agent_creation():
    """Test creating an agent."""
    agent = Agent("Test", "Developer", ["Python", "Testing"])
    assert agent.name == "Test"
    assert agent.role == "Developer"
    assert len(agent.expertise) == 2
    assert agent.get_contribution_count() == 0
    print("✅ test_agent_creation passed")


def test_agent_introduction():
    """Test agent introduction."""
    agent = Agent("Alice", "Manager", ["Leadership"])
    intro = agent.introduce()
    assert "Alice" in intro
    assert "Manager" in intro
    assert "Leadership" in intro
    print("✅ test_agent_introduction passed")


def test_agent_contribution():
    """Test agent making a contribution."""
    agent = Agent("Bob", "Analyst")
    contribution = agent.contribute("Test Topic", "My opinion")
    assert contribution["agent"] == "Bob"
    assert contribution["topic"] == "Test Topic"
    assert contribution["opinion"] == "My opinion"
    assert agent.get_contribution_count() == 1
    print("✅ test_agent_contribution passed")


def test_boardroom_creation():
    """Test creating a boardroom."""
    boardroom = Boardroom("Test Boardroom")
    assert boardroom.name == "Test Boardroom"
    assert len(boardroom.agents) == 0
    assert len(boardroom.discussions) == 0
    print("✅ test_boardroom_creation passed")


def test_add_agent_to_boardroom():
    """Test adding agents to boardroom."""
    boardroom = Boardroom()
    agent1 = Agent("Agent1", "Role1")
    agent2 = Agent("Agent2", "Role2")
    
    boardroom.add_agent(agent1)
    boardroom.add_agent(agent2)
    
    assert len(boardroom.agents) == 2
    assert boardroom.get_agent("Agent1") == agent1
    assert boardroom.get_agent("Agent2") == agent2
    print("✅ test_add_agent_to_boardroom passed")


def test_duplicate_agent_error():
    """Test that duplicate agent names raise an error."""
    boardroom = Boardroom()
    agent1 = Agent("Duplicate", "Role1")
    agent2 = Agent("Duplicate", "Role2")
    
    boardroom.add_agent(agent1)
    
    try:
        boardroom.add_agent(agent2)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "already exists" in str(e)
        print("✅ test_duplicate_agent_error passed")


def test_remove_agent():
    """Test removing an agent from boardroom."""
    boardroom = Boardroom()
    agent = Agent("ToRemove", "Role")
    
    boardroom.add_agent(agent)
    assert len(boardroom.agents) == 1
    
    result = boardroom.remove_agent("ToRemove")
    assert result is True
    assert len(boardroom.agents) == 0
    
    result = boardroom.remove_agent("NonExistent")
    assert result is False
    print("✅ test_remove_agent passed")


def test_discussion_flow():
    """Test the complete discussion flow."""
    boardroom = Boardroom()
    agent1 = Agent("Speaker1", "Role1")
    agent2 = Agent("Speaker2", "Role2")
    
    boardroom.add_agent(agent1)
    boardroom.add_agent(agent2)
    
    # Start discussion
    discussion = boardroom.start_discussion("Test Topic")
    assert discussion["topic"] == "Test Topic"
    assert len(boardroom.discussions) == 1
    
    # Add contributions
    boardroom.add_contribution("Speaker1", "Opinion 1")
    boardroom.add_contribution("Speaker2", "Opinion 2")
    
    assert len(boardroom.discussions[0]["contributions"]) == 2
    assert len(boardroom.discussions[0]["participants"]) == 2
    
    # Get summary
    summary = boardroom.get_discussion_summary()
    assert "Test Topic" in summary
    assert "Speaker1" in summary
    assert "Speaker2" in summary
    print("✅ test_discussion_flow passed")


def test_contribution_without_discussion():
    """Test that contribution without discussion raises error."""
    boardroom = Boardroom()
    agent = Agent("Agent", "Role")
    boardroom.add_agent(agent)
    
    try:
        boardroom.add_contribution("Agent", "Opinion")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "No active discussion" in str(e)
        print("✅ test_contribution_without_discussion passed")


def test_contribution_from_unknown_agent():
    """Test that contribution from unknown agent raises error."""
    boardroom = Boardroom()
    boardroom.start_discussion("Topic")
    
    try:
        boardroom.add_contribution("UnknownAgent", "Opinion")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("✅ test_contribution_from_unknown_agent passed")


def test_what_will_you_do():
    """Test the what_will_you_do_agent_bhai function."""
    result = what_will_you_do_agent_bhai()
    assert isinstance(result, str)
    assert "Agent Bhai" in result
    assert len(result) > 0
    print("✅ test_what_will_you_do passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*70)
    print("🧪 Running AI Boardroom Tests")
    print("="*70 + "\n")
    
    tests = [
        test_agent_creation,
        test_agent_introduction,
        test_agent_contribution,
        test_boardroom_creation,
        test_add_agent_to_boardroom,
        test_duplicate_agent_error,
        test_remove_agent,
        test_discussion_flow,
        test_contribution_without_discussion,
        test_contribution_from_unknown_agent,
        test_what_will_you_do,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"✅ Tests passed: {passed}")
    print(f"❌ Tests failed: {failed}")
    print(f"📊 Total tests: {passed + failed}")
    print("="*70 + "\n")
    
    if failed == 0:
        print("🎉 All tests passed successfully!")
        return 0
    else:
        print("⚠️  Some tests failed. Please review.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
