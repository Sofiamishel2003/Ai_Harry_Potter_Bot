Here is a README file for your Harry Potter AI bot repository:

---

# Harry Potter Bot

This repository contains a Harry Potter-themed chatbot powered by AI. The bot uses natural language processing to answer user queries related to the Harry Potter universe, using data scraped from the Harry Potter Fandom wiki.

## Features

- **Interactive Q&A**: Users can input prompts related to Harry Potter, and the bot provides relevant answers.
- **Sources**: Each answer includes sources from where the information was retrieved.
- **Streamlit Interface**: A simple and user-friendly web interface for interacting with the bot.
- **Integration with Pinecone**: The bot uses Pinecone for vector storage, enabling efficient retrieval of relevant information.

## Installation

### Prerequisites
- Python 3.x
- [Pinecone](https://www.pinecone.io/) account and API key
- OpenAI account and API key
- [Streamlit](https://streamlit.io/)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/harry-potter-bot.git
   cd harry-potter-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add the following environment variables:
   ```bash
   FIRE_CRAWL_API_KEY=<your_firecrawl_api_key>
   OPENAI_API_KEY=<your_openai_api_key>
   ```

4. Set up Pinecone and create an index with the name specified in `consts.py` (`firecrawl-harry-potter-index`).

5. Run the ingestion script to scrape and index Harry Potter-related data:
   ```bash
   python ingestion.py
   ```

6. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Usage

- Open the Streamlit app, and you will see a text input where you can type your Harry Potter-related questions.
- The bot will generate responses based on the indexed data and display the source of the information.

## File Structure

- `ingestion.py`: Handles scraping of Harry Potter data from external sources and ingestion into Pinecone.
- `main.py`: Contains the Streamlit frontend and manages user interaction with the chatbot.
- `consts.py`: Defines constants such as the Pinecone index name.

## Dependencies

- LangChain
- Pinecone
- OpenAI
- Streamlit
- Python-dotenv

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
![image](https://github.com/user-attachments/assets/a4075919-35be-48f8-b0a0-08efdf45775c)
![image](https://github.com/user-attachments/assets/b0deea50-b4aa-465c-81c8-02f60a65ece7)

