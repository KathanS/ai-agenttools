# AI AgentTools

Comprehensive Semantic Kernel plugins for AI agents to perform PC tasks: File I/O, Office documents (Excel, Word, PowerPoint), PDF operations, CSV/data manipulation, web scraping, and shell commands.

## Installation

```bash
pip install ai-agenttools
```

### Optional Dependencies

Install specific tool categories as needed:

```bash
# All tools
pip install ai-agenttools[all]

# Office suite (Excel, Word, PowerPoint)
pip install ai-agenttools[office]

# Individual tools
pip install ai-agenttools[excel]      # Excel operations
pip install ai-agenttools[word]       # Word documents
pip install ai-agenttools[powerpoint] # PowerPoint presentations
pip install ai-agenttools[pdf]        # PDF operations
pip install ai-agenttools[csv]        # CSV/data manipulation
pip install ai-agenttools[web]        # Web scraping
```

## Usage

```python
from agenttools import (
    FileIOTools,
    ExcelTools,
    WordTools,
    PowerPointTools,
    PDFTools,
    CSVTools,
    WebTools,
    ShellTool
)
from semantic_kernel import Kernel

kernel = Kernel()

# Add plugins as needed
kernel.add_plugin(FileIOTools(), plugin_name="file_io_tools")
kernel.add_plugin(ExcelTools(), plugin_name="excel_tools")
kernel.add_plugin(WordTools(), plugin_name="word_tools")
kernel.add_plugin(PowerPointTools(), plugin_name="powerpoint_tools")
kernel.add_plugin(PDFTools(), plugin_name="pdf_tools")
kernel.add_plugin(CSVTools(), plugin_name="csv_tools")
kernel.add_plugin(WebTools(), plugin_name="web_tools")
kernel.add_plugin(ShellTool(), plugin_name="shell_tool")
```

## Features

### FileIOTools (4 functions)
- `ensure_dir` - Create directories
- `write_file` - Write text files
- `append_file` - Append to files
- `read_file` - Read text files

### ExcelTools (15+ functions)
- `create_workbook` - Create Excel files
- `read_sheet` - Read Excel data
- `write_cell` - Write to cells
- `write_rows` - Write multiple rows
- `add_sheet`, `delete_sheet` - Manage worksheets
- `get_cell_value`, `set_cell_value` - Cell operations
- And more...

### WordTools (9 functions)
- `create_word_document` - Create Word documents
- `add_heading` - Add headings with levels
- `add_paragraph` - Add text paragraphs
- `add_table` - Create tables
- `set_table_cell` - Fill table cells
- `add_bullet_list` - Add bulleted lists
- `add_page_break` - Insert page breaks
- `read_word_document` - Extract text

### PowerPointTools (8 functions)
- `create_presentation` - Create PowerPoint files
- `add_title_slide` - Add title slides
- `add_content_slide` - Add slides with bullet points
- `add_blank_slide` - Add blank slides
- `add_text_box` - Add text boxes to slides
- `get_slide_count` - Count slides
- `read_slide_text` - Extract slide content

### PDFTools (8 functions)
- `create_pdf` - Create PDF documents
- `extract_pdf_text` - Extract text from PDFs
- `merge_pdfs` - Merge multiple PDFs
- `split_pdf` - Split PDF into pages
- `extract_pdf_page` - Extract specific pages
- `get_pdf_info` - Get PDF metadata
- `rotate_pdf_pages` - Rotate PDF pages

### CSVTools (9 functions)
- `read_csv` - Read CSV files
- `get_csv_info` - Get CSV metadata
- `filter_csv` - Filter rows by column value
- `sort_csv` - Sort by column
- `get_column_stats` - Statistical analysis
- `merge_csv_files` - Combine multiple CSVs
- `select_csv_columns` - Select specific columns
- `convert_csv_to_json` - CSV to JSON conversion

### WebTools (9 functions)
- `fetch_webpage` - Download HTML content
- `extract_text_from_url` - Extract text from webpages
- `extract_links` - Get all hyperlinks
- `extract_images` - Get all image URLs
- `download_file` - Download files from URLs
- `make_get_request` - HTTP GET requests
- `make_post_request` - HTTP POST requests
- `find_elements_by_tag` - Find HTML elements

### ShellTool (1 function)
- `run_shell` - Execute shell commands with safety checks
  - Blocks dangerous commands (rm -rf, etc.)

## License

**CC BY-NC 4.0** - Free for non-commercial use. For commercial licensing, please contact the author.

This software is provided for personal, educational, and research use only. Commercial use requires a separate license.

## Links

- PyPI: https://pypi.org/project/ai-agenttools/
- GitHub: https://github.com/KathanS/ai-agenttools
