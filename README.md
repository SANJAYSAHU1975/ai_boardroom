# AI Boardroom 🎯

A simple yet powerful Python framework for creating and managing AI agents in a collaborative boardroom setting.

## What Will Agent Bhai Do? 🤔

Agent Bhai facilitates AI-powered boardroom discussions by:

- 🤝 **Managing Multiple Agents**: Create agents with different roles and expertise
- 💬 **Facilitating Discussions**: Enable structured conversations on various topics
- 📊 **Tracking Contributions**: Record and analyze agent participation
- 🎯 **Collaborative Decision Making**: Bring diverse AI perspectives together
- 📝 **Generating Summaries**: Provide clear summaries of boardroom discussions

## Features ✨

- **Simple Agent System**: Easy-to-use `Agent` class for creating AI participants
- **Boardroom Management**: `Boardroom` class to orchestrate multiple agents
- **Discussion Tracking**: Keep records of all topics and contributions
- **Zero External Dependencies**: Pure Python implementation
- **Extensible Design**: Easy to customize for your specific needs

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/SANJAYSAHU1975/ai_boardroom.git
cd ai_boardroom
```

2. No additional dependencies required! Just use Python 3.6+

## Quick Start 💻

### Basic Usage

```python
from agent_bhai import Agent, Boardroom

# Create a boardroom
boardroom = Boardroom("My AI Boardroom")

# Create agents
ceo = Agent("Rajesh", "CEO", ["Strategy", "Leadership"])
cto = Agent("Priya", "CTO", ["Technology", "Innovation"])

# Add agents to boardroom
boardroom.add_agent(ceo)
boardroom.add_agent(cto)

# Start a discussion
boardroom.start_discussion("Should we adopt microservices architecture?")

# Agents contribute
boardroom.add_contribution("Rajesh", "This aligns with our scaling strategy.")
boardroom.add_contribution("Priya", "Technically feasible and beneficial long-term.")

# Get summary
print(boardroom.get_discussion_summary())
```

### Run the Example

```bash
python example.py
```

This will run a complete demonstration showing:
- Creating a boardroom
- Adding multiple agents with different roles
- Starting a discussion
- Collecting opinions from all agents
- Generating a discussion summary

## API Reference 📚

### Agent Class

```python
Agent(name: str, role: str, expertise: List[str] = None)
```

**Methods:**
- `introduce()` - Returns an introduction of the agent
- `contribute(topic, opinion)` - Make a contribution to a discussion
- `get_contribution_count()` - Get number of contributions made

### Boardroom Class

```python
Boardroom(name: str = "AI Boardroom")
```

**Methods:**
- `add_agent(agent)` - Add an agent to the boardroom
- `remove_agent(agent_name)` - Remove an agent by name
- `get_agent(agent_name)` - Get an agent by name
- `start_discussion(topic)` - Start a new discussion
- `add_contribution(agent_name, opinion)` - Add a contribution to current discussion
- `get_discussion_summary(index)` - Get formatted summary of a discussion
- `list_agents()` - List all agents in the boardroom

## Example Output 📺

```
Agent Bhai can do the following:

1. 🤝 Join the Boardroom: Create and manage AI agents with different roles
2. 💬 Facilitate Discussions: Enable agents to discuss topics and share opinions
3. 📊 Track Contributions: Keep record of all agent contributions
4. 🎯 Collaborate: Allow multiple agents to work together on decisions
5. 📝 Summarize Meetings: Generate summaries of boardroom discussions
6. 🌟 Demonstrate Leadership: Each agent brings unique expertise to the table
```

## Use Cases 🎪

- **Team Decision Making**: Simulate different perspectives in business decisions
- **AI Collaboration**: Create multi-agent systems for complex problem solving
- **Educational Tool**: Teach concepts of multi-agent systems
- **Prototyping**: Quick prototyping of AI agent interactions
- **Discussion Facilitation**: Structure and track group discussions

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License 📄

This project is open source and available under the MIT License.

## Author 👨‍💻

Created by SANJAYSAHU1975

---

**Question:** *What will you do agent bhai?*  
**Answer:** *Agent Bhai will bring your AI agents together and make them collaborate! 🚀*