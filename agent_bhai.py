"""
AI Boardroom - A simple AI agent framework

This module provides a basic framework for creating and managing AI agents
in a boardroom setting where multiple agents can collaborate.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime


class Agent:
    """
    Base Agent class representing an AI agent in the boardroom.
    
    Each agent has a name, role, and can contribute to discussions.
    """
    
    def __init__(self, name: str, role: str, expertise: Optional[List[str]] = None):
        """
        Initialize an Agent.
        
        Args:
            name: The name of the agent
            role: The role/designation of the agent (e.g., "CEO", "CTO", "CFO")
            expertise: List of areas of expertise
        """
        self.name = name
        self.role = role
        self.expertise = expertise or []
        self.contributions = []
        
    def introduce(self) -> str:
        """Return an introduction of the agent."""
        expertise_str = ", ".join(self.expertise) if self.expertise else "General"
        return f"Namaste! I'm {self.name}, the {self.role}. My expertise includes: {expertise_str}"
    
    def contribute(self, topic: str, opinion: str) -> Dict[str, Any]:
        """
        Make a contribution to a discussion.
        
        Args:
            topic: The topic being discussed
            opinion: The agent's opinion/contribution
            
        Returns:
            A dictionary containing the contribution details
        """
        contribution = {
            "agent": self.name,
            "role": self.role,
            "topic": topic,
            "opinion": opinion,
            "timestamp": datetime.now().isoformat()
        }
        self.contributions.append(contribution)
        return contribution
    
    def get_contribution_count(self) -> int:
        """Return the number of contributions made by this agent."""
        return len(self.contributions)
    
    def __str__(self) -> str:
        return f"Agent(name={self.name}, role={self.role})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Boardroom:
    """
    Boardroom class to manage multiple agents and facilitate discussions.
    """
    
    def __init__(self, name: str = "AI Boardroom"):
        """
        Initialize a Boardroom.
        
        Args:
            name: The name of the boardroom
        """
        self.name = name
        self.agents: List[Agent] = []
        self.discussions: List[Dict[str, Any]] = []
        
    def add_agent(self, agent: Agent) -> None:
        """
        Add an agent to the boardroom.
        
        Args:
            agent: The Agent instance to add
        """
        if not isinstance(agent, Agent):
            raise TypeError("Only Agent instances can be added to the boardroom")
        
        # Check if agent with same name already exists
        if any(a.name == agent.name for a in self.agents):
            raise ValueError(f"Agent with name '{agent.name}' already exists in the boardroom")
            
        self.agents.append(agent)
        
    def remove_agent(self, agent_name: str) -> bool:
        """
        Remove an agent from the boardroom.
        
        Args:
            agent_name: The name of the agent to remove
            
        Returns:
            True if agent was removed, False if not found
        """
        for i, agent in enumerate(self.agents):
            if agent.name == agent_name:
                self.agents.pop(i)
                return True
        return False
    
    def get_agent(self, agent_name: str) -> Optional[Agent]:
        """
        Get an agent by name.
        
        Args:
            agent_name: The name of the agent
            
        Returns:
            The Agent instance if found, None otherwise
        """
        for agent in self.agents:
            if agent.name == agent_name:
                return agent
        return None
    
    def start_discussion(self, topic: str) -> Dict[str, Any]:
        """
        Start a new discussion on a topic.
        
        Args:
            topic: The topic for discussion
            
        Returns:
            A dictionary containing the discussion details
        """
        discussion = {
            "topic": topic,
            "started_at": datetime.now().isoformat(),
            "contributions": [],
            "participants": []
        }
        self.discussions.append(discussion)
        return discussion
    
    def add_contribution(self, agent_name: str, opinion: str) -> Optional[Dict[str, Any]]:
        """
        Add a contribution from an agent to the current discussion.
        
        Args:
            agent_name: The name of the agent making the contribution
            opinion: The agent's opinion/contribution
            
        Returns:
            The contribution dictionary if successful, None otherwise
        """
        if not self.discussions:
            raise ValueError("No active discussion. Start a discussion first.")
            
        agent = self.get_agent(agent_name)
        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found in the boardroom")
        
        current_discussion = self.discussions[-1]
        contribution = agent.contribute(current_discussion["topic"], opinion)
        current_discussion["contributions"].append(contribution)
        
        if agent_name not in current_discussion["participants"]:
            current_discussion["participants"].append(agent_name)
            
        return contribution
    
    def get_discussion_summary(self, discussion_index: int = -1) -> str:
        """
        Get a summary of a discussion.
        
        Args:
            discussion_index: The index of the discussion (default: -1 for latest)
            
        Returns:
            A formatted string summarizing the discussion
        """
        if not self.discussions:
            return "No discussions have taken place yet."
            
        discussion = self.discussions[discussion_index]
        summary = [
            f"\n{'='*60}",
            f"Discussion Topic: {discussion['topic']}",
            f"Started at: {discussion['started_at']}",
            f"Participants: {', '.join(discussion['participants'])}",
            f"Total Contributions: {len(discussion['contributions'])}",
            f"{'='*60}\n"
        ]
        
        for i, contrib in enumerate(discussion['contributions'], 1):
            summary.append(f"{i}. {contrib['agent']} ({contrib['role']}):")
            summary.append(f"   {contrib['opinion']}\n")
            
        return "\n".join(summary)
    
    def list_agents(self) -> str:
        """
        List all agents in the boardroom.
        
        Returns:
            A formatted string listing all agents
        """
        if not self.agents:
            return "No agents in the boardroom yet."
            
        lines = [f"\n{self.name} - Current Members:", "=" * 60]
        for agent in self.agents:
            lines.append(f"- {agent.name} ({agent.role})")
            if agent.expertise:
                lines.append(f"  Expertise: {', '.join(agent.expertise)}")
        lines.append("=" * 60)
        return "\n".join(lines)
    
    def __str__(self) -> str:
        return f"Boardroom(name={self.name}, agents={len(self.agents)}, discussions={len(self.discussions)})"
    
    def __repr__(self) -> str:
        return self.__str__()


def what_will_you_do_agent_bhai() -> str:
    """
    Answer the question: 'what will you do agent bhai'
    
    This function demonstrates the capabilities of the agent system.
    
    Returns:
        A string describing what the agent can do
    """
    return """
Agent Bhai can do the following:

1. 🤝 Join the Boardroom: Create and manage AI agents with different roles
2. 💬 Facilitate Discussions: Enable agents to discuss topics and share opinions
3. 📊 Track Contributions: Keep record of all agent contributions
4. 🎯 Collaborate: Allow multiple agents to work together on decisions
5. 📝 Summarize Meetings: Generate summaries of boardroom discussions
6. 🌟 Demonstrate Leadership: Each agent brings unique expertise to the table

Agent Bhai is here to help manage your AI boardroom! 🚀
"""


if __name__ == "__main__":
    print("=" * 60)
    print("Welcome to AI Boardroom!")
    print("=" * 60)
    print(what_will_you_do_agent_bhai())
