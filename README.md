# Tailor Trailers

Tailor Trailer is an AI-powered application that generates tailored movie trailers for different audience segments. It uses agentic workflows to analyze movie transcripts, identify audience segments, extract key scenes, and create engaging trailers.

## Features
- Upload movie transcripts and video files.
- AI-driven audience segmentation and trailer generation.
- Automated video trimming and merging.
- Streamlit-based user interface for ease of use.
- Uses `crewai`, `langchain_groq`, and custom tools for AI-powered processing.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/tailor-trailer.git
   cd tailor-trailer
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Activate the virtual environment:
   ```sh
   poetry shell
   ```
4. Set up environment variables:
   ```sh
   export GROQ_API_KEY=your_api_key
   ```

## Usage

1. Run the application:
   ```sh
   streamlit run main.py
   ```
2. Open the app in your browser and follow these steps:
   - Enter the movie name and genre.
   - Upload the movie transcript (TXT) and video file (MP4).
   - Click "Generate Trailers" and wait for the AI agents to process the data.
   - Download the generated trailers.

## How It Works

### Agentic Workflow
The application consists of three AI agents:
1. **Movie Director Agent** - Analyzes the transcript and identifies audience segments.
2. **Junior Video Editor Agent** - Trims key scenes based on timestamps.
3. **Senior Video Editor Agent** - Merges trimmed clips into final trailers.

### Tools Used
- `crewai` - Agent-based AI automation.
- `langchain_groq` - LLM for NLP processing.
- `Streamlit` - Web interface.

## Folder Structure
```
Tailor-Trailer/
│── main.py                # Main application file
│── tools/
│   ├── video_tools.py     # Video trimming and merging utilities
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
```

## Future Improvements
- Support for more file formats (e.g., subtitles, additional video codecs).
- Customizable trailer styles and themes.
- Improved AI-based video enhancement.

## License
This project is licensed under the MIT License.

## Contact
Developed by Ranveer Singh Ranawat. For queries or collaborations, feel free to reach out at ranawatranveer0323@gmail.com :)

