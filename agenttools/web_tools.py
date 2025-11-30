"""Web scraping and HTTP request tools using requests and BeautifulSoup."""

from typing import Annotated
from semantic_kernel.functions import kernel_function

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False


class WebTools:
    """Tools for web scraping and HTTP requests."""

    def __init__(self):
        """Initialize WebTools."""
        if not REQUESTS_AVAILABLE:
            print("Warning: requests not installed. Install with: pip install requests")
        if not BS4_AVAILABLE:
            print("Warning: beautifulsoup4 not installed. Install with: pip install beautifulsoup4")

    @kernel_function(
        name="fetch_webpage",
        description="Fetch the HTML content of a webpage"
    )
    def fetch_webpage(
        self,
        url: Annotated[str, "URL of the webpage to fetch"]
    ) -> Annotated[str, "HTML content or error message"]:
        """Fetch raw HTML content from a URL."""
        if not REQUESTS_AVAILABLE:
            return "Error: requests is not installed"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as err:
            return f"Error fetching webpage: {str(err)}"

    @kernel_function(
        name="extract_text_from_url",
        description="Extract all text content from a webpage"
    )
    def extract_text_from_url(
        self,
        url: Annotated[str, "URL of the webpage"]
    ) -> Annotated[str, "Extracted text or error message"]:
        """Extract and return all text from a webpage."""
        if not REQUESTS_AVAILABLE or not BS4_AVAILABLE:
            return "Error: requests and beautifulsoup4 are required"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text(separator='\n', strip=True)
            return text
        except Exception as err:
            return f"Error extracting text: {str(err)}"

    @kernel_function(
        name="extract_links",
        description="Extract all links from a webpage"
    )
    def extract_links(
        self,
        url: Annotated[str, "URL of the webpage"]
    ) -> Annotated[str, "List of links or error message"]:
        """Extract all hyperlinks from a webpage."""
        if not REQUESTS_AVAILABLE or not BS4_AVAILABLE:
            return "Error: requests and beautifulsoup4 are required"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                text = link.get_text(strip=True)
                links.append(f"{text}: {href}")
            
            return "\n".join(links) if links else "No links found"
        except Exception as err:
            return f"Error extracting links: {str(err)}"

    @kernel_function(
        name="download_file",
        description="Download a file from a URL"
    )
    def download_file(
        self,
        url: Annotated[str, "URL of the file to download"],
        output_path: Annotated[str, "Path where the file will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Download a file from a URL and save it locally."""
        if not REQUESTS_AVAILABLE:
            return "Error: requests is not installed"
        
        try:
            response = requests.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return f"File downloaded successfully to: {output_path}"
        except Exception as err:
            return f"Error downloading file: {str(err)}"

    @kernel_function(
        name="make_get_request",
        description="Make an HTTP GET request to an API endpoint"
    )
    def make_get_request(
        self,
        url: Annotated[str, "URL of the API endpoint"],
        params: Annotated[str, "Query parameters as key=value pairs, comma-separated"] = ""
    ) -> Annotated[str, "Response content or error message"]:
        """Make an HTTP GET request to an API."""
        if not REQUESTS_AVAILABLE:
            return "Error: requests is not installed"
        
        try:
            query_params = {}
            if params:
                for pair in params.split(','):
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        query_params[key.strip()] = value.strip()
            
            response = requests.get(url, params=query_params, timeout=10)
            response.raise_for_status()
            
            return response.text
        except Exception as err:
            return f"Error making GET request: {str(err)}"

    @kernel_function(
        name="make_post_request",
        description="Make an HTTP POST request to an API endpoint"
    )
    def make_post_request(
        self,
        url: Annotated[str, "URL of the API endpoint"],
        data: Annotated[str, "Data to send as key=value pairs, comma-separated"] = ""
    ) -> Annotated[str, "Response content or error message"]:
        """Make an HTTP POST request to an API."""
        if not REQUESTS_AVAILABLE:
            return "Error: requests is not installed"
        
        try:
            post_data = {}
            if data:
                for pair in data.split(','):
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        post_data[key.strip()] = value.strip()
            
            response = requests.post(url, data=post_data, timeout=10)
            response.raise_for_status()
            
            return response.text
        except Exception as err:
            return f"Error making POST request: {str(err)}"

    @kernel_function(
        name="extract_images",
        description="Extract all image URLs from a webpage"
    )
    def extract_images(
        self,
        url: Annotated[str, "URL of the webpage"]
    ) -> Annotated[str, "List of image URLs or error message"]:
        """Extract all image URLs from a webpage."""
        if not REQUESTS_AVAILABLE or not BS4_AVAILABLE:
            return "Error: requests and beautifulsoup4 are required"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            images = []
            
            for img in soup.find_all('img'):
                src = img.get('src')
                alt = img.get('alt', 'No alt text')
                if src:
                    images.append(f"{alt}: {src}")
            
            return "\n".join(images) if images else "No images found"
        except Exception as err:
            return f"Error extracting images: {str(err)}"

    @kernel_function(
        name="find_elements_by_tag",
        description="Find all elements with a specific HTML tag on a webpage"
    )
    def find_elements_by_tag(
        self,
        url: Annotated[str, "URL of the webpage"],
        tag: Annotated[str, "HTML tag to search for (e.g., 'h1', 'p', 'div')"]
    ) -> Annotated[str, "List of elements or error message"]:
        """Find all elements with a specific HTML tag."""
        if not REQUESTS_AVAILABLE or not BS4_AVAILABLE:
            return "Error: requests and beautifulsoup4 are required"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(tag)
            
            results = []
            for i, elem in enumerate(elements, 1):
                text = elem.get_text(strip=True)
                results.append(f"{i}. {text}")
            
            return "\n".join(results) if results else f"No <{tag}> elements found"
        except Exception as err:
            return f"Error finding elements: {str(err)}"
