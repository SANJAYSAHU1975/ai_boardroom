#!/usr/bin/env python3
"""
Example demonstration of the AI Boardroom system.

This script shows how to use the Agent and Boardroom classes
to create a simple AI boardroom discussion.
"""

from agent_bhai import Agent, Boardroom, what_will_you_do_agent_bhai


def main():
    """Run the AI Boardroom demonstration."""
    
    print("\n" + "="*70)
    print("🎯 AI BOARDROOM DEMONSTRATION 🎯")
    print("="*70)
    
    # Show what Agent Bhai can do
    print(what_will_you_do_agent_bhai())
    
    # Create a boardroom
    print("\n📍 Step 1: Creating the Boardroom...")
    boardroom = Boardroom("Tech Startup Boardroom")
    print(f"✅ Created: {boardroom}")
    
    # Create agents with different roles
    print("\n📍 Step 2: Adding Agents to the Boardroom...")
    
    agents = [
        Agent("Rajesh", "CEO", ["Strategy", "Vision", "Leadership"]),
        Agent("Priya", "CTO", ["Technology", "Architecture", "Innovation"]),
        Agent("Amit", "CFO", ["Finance", "Investment", "Risk Management"]),
        Agent("Neha", "CMO", ["Marketing", "Branding", "Customer Engagement"])
    ]
    
    for agent in agents:
        boardroom.add_agent(agent)
        print(f"✅ {agent.introduce()}")
    
    # List all agents
    print(boardroom.list_agents())
    
    # Start a discussion
    print("\n📍 Step 3: Starting a Discussion...")
    topic = "Should we invest in AI technology for our product?"
    discussion = boardroom.start_discussion(topic)
    print(f"✅ Discussion started: '{topic}'")
    
    # Agents contribute to the discussion
    print("\n📍 Step 4: Agents Contributing Their Opinions...")
    
    contributions = [
        ("Rajesh", "As CEO, I believe investing in AI is crucial for our long-term vision. "
                   "It aligns with market trends and will give us a competitive advantage."),
        ("Priya", "From a technical perspective, AI integration is feasible. "
                  "We have the infrastructure, and it will significantly enhance our product capabilities."),
        ("Amit", "Financially, we need to allocate 20% of our Q4 budget. "
                 "ROI projections show positive returns within 18 months. I support this investment."),
        ("Neha", "Marketing-wise, AI features will be a major selling point. "
                 "Our customer surveys show 75% interest in AI-powered features. This is a win!")
    ]
    
    for agent_name, opinion in contributions:
        boardroom.add_contribution(agent_name, opinion)
        print(f"💬 {agent_name} has contributed to the discussion")
    
    # Display discussion summary
    print("\n📍 Step 5: Discussion Summary...")
    summary = boardroom.get_discussion_summary()
    print(summary)
    
    # Show agent statistics
    print("\n📍 Step 6: Agent Statistics...")
    print("="*70)
    for agent in boardroom.agents:
        print(f"📊 {agent.name} ({agent.role}): {agent.get_contribution_count()} contribution(s)")
    print("="*70)
    
    # Conclusion
    print("\n" + "="*70)
    print("✨ DEMONSTRATION COMPLETE! ✨")
    print("="*70)
    print("\n💡 Agent Bhai has successfully facilitated the boardroom discussion!")
    print("🎉 All agents participated and shared their expertise!\n")


if __name__ == "__main__":
    main()
