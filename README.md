# Sales-Data-Analysis

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

------------------------------------

### Built With

This section should list any major frameworks that you built your project using:
* conda >=4.7.12
* python 3
* numpy
* pandas==1.3.0
* matplotlib==3.3.4
* seaborn==0.11.1
* fpdf==1.7.2

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running install conda and follow these simple steps.

### Installation

1. Clone the repo: https://github.com/rashikcs/Sales-Data-Analysis.git

2. - Install required packages packages by going to the project folder and type this from command prompt
   ```sh
   conda env update -f environments.yml 
   ```
   ```
This will create a new conda environment named **data_analysis_env**.<br />
Activate this environment from shell by typing
   ```sh
   conda activate data_analysis_env
   ```
Run specific Jupyter Notebook files after activating the environment.
   ```sh
   jupyter notebook
   ```