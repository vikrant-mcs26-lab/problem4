# Executing the Code
## Pre-Requisite 
1. Python Environment. Refer [Setting Up](#setting-up)
1. Pre generated graph files from previous problems. Stored in following  directory structure. (Already present in the project)
```
resources
├── graphs
│   ├── graph_10.graph
│   ├── graph_15.graph
│   ├── graph_20.graph
│   ├── graph_25.graph
│   ├── graph_30.graph
│   ├── graph_35.graph
│   ├── graph_40.graph
│   └── graph_45.graph
└── vertex
    ├── graph_10.vertex_cover
    ├── graph_15.vertex_cover
    ├── graph_20.vertex_cover
    ├── graph_25.vertex_cover
    ├── graph_30.vertex_cover
    ├── graph_35.vertex_cover
    ├── graph_40.vertex_cover
    └── graph_45.vertex_cover
```

## Execution
If running on unix like operating system, run the following, from the root directory (i.e. same directory as this file)
```
python main.py --node10 ./resources_nodes10 --node20 ./resources_nodes20
```

Output would be available in 
- `./resources_node10/lpp_approx` directory, it would contain approximation of vertex cover along with accounting information
- `./resources_node10/image` directory, it would contain all the image file representing Optimal Vertex Cover, and Approximated Vertex Cover. 
- `./resources_node10/table.csv` 
- `./resources_node20/lpp_approx` directory, it would contain approximation of vertex cover along with accounting information
- `./resources_node20/image` directory, it would contain all the image file representing Optimal Vertex Cover, and Approximated Vertex Cover. 
- `./resources_node20/table.csv`.

# Setting Up
In the root directory of project (i.e. problem1), run following commands to setup python 
```bash
python -m venv venv
source venv/bin/activate
pip install -r ./requirement.txt
```

Run these commands instead if you are running it on windows host. 
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r ./python/requirement.txt
```