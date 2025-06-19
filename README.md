# YouTube_Data_Scraper
This repository contains Python code for a web scraper designed to extract data from YouTube. It leverages DrissionPage for browser automation and BeautifulSoup for parsing HTML content.
---

用于从 YouTube 抓取视频信息的 Python 网页爬虫。它利用 `DrissionPage` 进行浏览器自动化，并使用 `BeautifulSoup` 解析 HTML 内容。

## Features (功能)

* **Video Listing Extraction (视频列表提取):** Gathers video titles, URLs, and upload dates from Youtube results (currently targeting "china travel" keywords). It handles continuous page scrolling to load more videos.
* **Detailed Video Information Retrieval (详细视频信息获取):** Navigates to individual video pages to extract additional details, including publisher name, view count, comment count, and video description.
* **Data Persistence (数据持久化):** Saves collected data incrementally to JSON files (`list_all.json`, `list.json`, `data.json`) to prevent data loss during scraping.
* **Data Export (数据导出):** Converts the collected data into a clean Excel spreadsheet (`youtube.xlsx`) for easy analysis.

---

* **视频列表提取：** 从 YouTube 搜索结果中（目前针对“china travel”关键词）收集视频标题、URL 和上传日期。它支持持续滚动页面以加载更多视频。
* **详细视频信息获取：** 导航到单个视频页面，提取发布者名称、播放量、评论数和视频简介等更多详细信息。
* **数据持久化：** 将收集到的数据增量保存到 JSON 文件（`list_all.json`、`list.json`、`data.json`）中，以防止抓取过程中数据丢失。
* **数据导出：** 将收集到的数据转换为整洁的 Excel 电子表格（`youtube.xlsx`），便于分析。

## How it Works (工作原理)

The script operates in three main stages:

1.  **`get_data()`:** Initiates a Chromium browser session (connected via `127.0.0.1:9220`), navigates to a Youtube results page, and continuously scrolls to load videos. It then parses the page to extract video titles, upload times, and links, saving unique entries to JSON files.
2.  **`get_detail()`:** Reads the video links from `list.json` and visits each link. For each video, it clicks to expand the description and extracts the publisher's name, view count, comment count, and video description, saving this detailed information to `data.json`. It also includes error handling for cases where elements might not be immediately available.
3.  **`save()`:** Reads the complete data from `data.json` and converts it into a pandas DataFrame, which is then exported to an Excel file named `youtube.xlsx`.

---

脚本主要分为三个阶段：

1.  **`get_data()`：** 启动一个 Chromium 浏览器会话（通过 `127.0.0.1:9220` 连接），导航到 YouTube 搜索结果页面，并持续滚动以加载视频。然后解析页面以提取视频标题、上传时间和链接，并将独特的条目保存到 JSON 文件中。
2.  **`get_detail()`：** 从 `list.json` 读取视频链接并访问每个链接。对于每个视频，它会点击展开描述，并提取发布者名称、播放量、评论数和视频描述，将这些详细信息保存到 `data.json`。它还包含了对某些元素可能无法立即获取时的错误处理。
3.  **`save()`：** 从 `data.json` 读取完整数据，并将其转换为 pandas DataFrame，然后导出到名为 `youtube.xlsx` 的 Excel 文件中。

## Setup (设置)

1.  **Dependencies (依赖项):** Install the required Python libraries using pip:
    ```bash
    pip install DrissionPage beautifulsoup4 pandas lxml
    ```
2.  **Chromium Browser (Chromium 浏览器):** Ensure you have a Chromium-based browser (like Chrome, Edge, Brave) installed on your system.
3.  **Launch Browser with Remote Debugging (启动带远程调试的浏览器):** You need to launch your Chromium browser with remote debugging enabled on a specific port (e.g., `9220`). This allows the Python script to connect and control it.

    **Example Command (示例命令):**
    ```bash
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9220 --user-data-dir="C:\ChromeProfile"
    ```
    *Replace the path with your actual Chrome/Chromium executable path.*
    *`--user-data-dir` is optional, it specifies a separate profile to avoid interference with your regular Browse sessions.*

    You can run this command in your command prompt (CMD) or terminal. The browser window will open, and you should keep it open while the script is running.

---

1.  **依赖项：** 使用 pip 安装所需的 Python 库：
    ```bash
    pip install DrissionPage beautifulsoup4 pandas lxml
    ```
2.  **Chromium 浏览器：** 确保您的系统上安装了基于 Chromium 内核的浏览器（如 Chrome、Edge、Brave 等）。
3.  **启动带远程调试的浏览器：** 您需要以特定的命令启动 Chromium 浏览器，使其在特定端口（例如 `9220`）上启用远程调试。这允许 Python 脚本连接并控制它。

    **示例命令：**
    ```bash
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9220 --user-data-dir="C:\ChromeProfile"
    ```
    *请将路径替换为您的 Chrome/Chromium 可执行文件的实际路径。*
    *`--user-data-dir` 是可选的，它指定一个单独的用户配置文件，以避免与您日常浏览会话冲突。*

    您可以在命令提示符（CMD）或终端中运行此命令。浏览器窗口将会打开，在脚本运行期间您应该保持它处于打开状态。

## Usage (使用方法)

1.  **Prepare your browser (准备您的浏览器):** Launch your Chromium browser with the remote debugging port as described in the "Setup" section.
2.  **Run the script (运行脚本):**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `main_scraper.py`)

The script will start collecting data and save it into the specified JSON and Excel files in the same directory.

---

1.  **准备您的浏览器：** 按照“设置”部分所述，启动带远程调试端口的 Chromium 浏览器。
2.  **运行脚本：**
    ```bash
    python 您的脚本名称.py
    ```
    （请将 `您的脚本名称.py` 替换为您的 Python 文件的实际名称，例如 `main_scraper.py`）

脚本将开始收集数据，并将其保存到同一目录中指定的 JSON 和 Excel 文件。

## Important Notes (重要提示)

* **Anti-Scraping Measures (反爬措施):** Websites like YouTube may have anti-scraping measures (e.g., IP blocks, CAPTCHAs, rate limiting). This script is a basic example and may require enhancements (like proxies or more sophisticated human-like behavior simulation) for large-scale or robust scraping.
* **Website Structure Changes (网站结构变化):** Websites frequently update their page structures. If YouTube changes its HTML element IDs or class names, the CSS selectors in the code (e.g., `.text-wrapper.style-scope.ytd-video-renderer`) will need to be updated accordingly.
* **Legal & Ethical Considerations (法律与道德考量):** Always respect website terms of service and relevant laws when performing web scraping. Avoid placing undue burden on target websites.

---
