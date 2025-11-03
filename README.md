# Cache Simulator - Computer Architecture Learning Project

## 📚 Project Overview
This is my computer architecture learning project where I implement a configurable cache simulator in Python. The goal is to understand how CPU caches work through hands-on implementation and experimentation.

**Project Timeline**: Started in December 2024, completed in September 2025

## 🎯 Learning Journey
This project took some time because:
- I was simultaneously learning Python programming
- Understanding computer architecture concepts was challenging
- I wanted to implement proper visualization and analysis
- It's a complex topic that required thorough understanding

## 🏗️ Project Structure
cache-simulator/
├── src/
│ ├── main.py # Main experiments
│ ├── cache.py # Cache implementation
│ ├── cache_config.py # Configuration
│ ├── replacement_policies.py # LRU, FIFO, Random
│ └── trace_generator.py # Memory access patterns
├── tests/
│ └── test_basic.py # Basic functionality tests
├── utils/
│ └── visualizer.py # Results visualization
├── traces/ # Memory access traces
├── requirements.txt
└── README.md

## 🚀 Features
- Configurable cache parameters (size, block size, associativity)
- Multiple replacement policies (LRU, FIFO, Random)
- Different memory access patterns
- Performance visualization and analysis
- Educational debugging tools

## 🛠️ Installation
```bash
# Create virtual environment
python -m venv cache_env
cache_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the simulator
python src/main.py 

# What I Learned
How CPU caches work in modern processors
Impact of different cache configurations on performance
Memory access patterns and locality
Data visualization for performance analysis
Object-oriented programming in Python

# Future Improvements
Add multi-level cache hierarchy
Implement write policies
Add more replacement algorithms
Create interactive visualizations


## **3. src/__init__.py**
```python
"""
Cache Simulator Package
My computer architecture learning project
Initial version: December 2024
"""

__version__ = "1.0.0"
__author__ = "Nikita"