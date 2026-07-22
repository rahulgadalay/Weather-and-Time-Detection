# 🏗️ System Architecture

## Overview

The Weather & Time Detection AI Agent is designed using a modular architecture that separates the AI reasoning layer from the tool execution layer. Google Agent Development Kit (ADK) acts as the orchestration framework, while Gemini is responsible for understanding user intent and selecting the appropriate tool.

This modular design makes the application easy to maintain, extend, and scale by allowing new tools to be added with minimal changes to the core agent.

---

# Architecture Diagram

```
                +----------------------+
                |        User          |
                +----------+-----------+
                           |
                           | Natural Language Query
                           v
                +----------------------+
                | Google ADK Agent     |
                +----------+-----------+
                           |
                           | Intent Analysis
                           v
                +----------------------+
                |   Gemini AI Model    |
                +----------+-----------+
                           |
            +--------------+--------------+
            |                             |
            |                             |
            v                             v
+-------------------------+     +-------------------------+
|      Weather Tool       |     |        Time Tool        |
+------------+------------+     +------------+------------+
             |                               |
             | API Request                   | API Request
             v                               v
+-------------------------+     +-------------------------+
|   Weather Service API   |     |   Time Service API      |
+------------+------------+     +------------+------------+
             |                               |
             +---------------+---------------+
                             |
                             v
                 +--------------------------+
                 |   Formatted AI Response  |
                 +------------+-------------+
                              |
                              v
                         Response to User
```

---

# Components

## 1. User

The user interacts with the application by entering natural language queries such as:

- What is the weather in Hyderabad?
- Tell me the current time in Tokyo.

The user does not need to specify which tool should be used.

---

## 2. Google ADK Agent

The Google Agent Development Kit (ADK) acts as the central controller of the application.

Its responsibilities include:

- Receiving user requests
- Managing available tools
- Communicating with Gemini
- Executing the selected tool
- Returning the final response

---

## 3. Gemini AI Model

Gemini is responsible for understanding the user's intent.

Instead of relying on keyword matching, Gemini determines:

- Whether the user is asking for weather information
- Whether the user is asking for the current time
- Which tool should be executed

This enables more natural and flexible user interactions.

---

## 4. Weather Tool

The Weather Tool handles all weather-related requests.

Responsibilities include:

- Receiving the city name
- Sending requests to the weather API
- Parsing the API response
- Returning formatted weather information

Example Output:

- Temperature
- Wind Speed
- Weather Condition

---

## 5. Time Tool

The Time Tool is responsible for retrieving the current local time.

Responsibilities include:

- Identifying the requested location
- Retrieving the current local time
- Formatting the response

---

## 6. External APIs

The application relies on external services for real-time information.

These services provide:

- Current weather data
- Current local time

Keeping the data external ensures that the information returned is always up to date.

---

# Request Flow

1. The user submits a natural language query.
2. Google ADK receives the request.
3. Gemini analyzes the user's intent.
4. ADK selects the appropriate tool.
5. The selected tool sends a request to the external API.
6. The API returns real-time data.
7. The tool formats the response.
8. ADK sends the final response back to the user.

---

# Design Principles

The project follows several software engineering best practices:

- Modular architecture
- Separation of concerns
- Reusable tools
- Easy scalability
- Secure configuration using environment variables
- Maintainable code structure

---

# Advantages

- Clean separation between AI reasoning and tool execution.
- Easy integration of additional tools.
- Modular Python codebase.
- Real-time information retrieval.
- Flexible natural language interaction.
- Scalable architecture for future enhancements.

---

# Future Improvements

The current architecture can be extended with additional tools, including:

- News Tool
- Currency Converter
- Email Assistant
- Calendar Integration
- PDF Question Answering
- Retrieval-Augmented Generation (RAG)
- Multi-Agent Collaboration
- Voice Interface

---

# Conclusion

The Weather & Time Detection AI Agent demonstrates how Google ADK and Gemini can be combined to build modular, tool-driven AI applications. By separating intent understanding from tool execution, the project provides a scalable foundation that can be expanded with additional capabilities while maintaining a clean and organized architecture.
