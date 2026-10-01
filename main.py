from graph import Graph
import argparse as cli
import pathlib as pth
from read_files import Data
from utils import visualise
import csv
from tqdm import trange

def parse_args() -> cli.Namespace:
    parser = cli.ArgumentParser("Finds Approx Vertex Cover")

    parser.add_argument(
        "--node10",
        type=str,
        # required=True,
        help="Resources Directory where all the input files of graph with node 10 are stored")

    parser.add_argument(
        "--node20",
        type=str,
        # required=True,
        help="Resources Directory where all the input files of graph with node 20 are stored")

    return parser.parse_known_args()[0]

def execute_for_res_dir(res_dir: pth.Path) -> None:
    output_dir = res_dir.joinpath("lpp_approx")
    output_dir.mkdir(exist_ok=True, parents=True)
    output_dir_img = res_dir.joinpath("image")
    output_dir_img.mkdir(exist_ok=True)

    graph_files = list(res_dir.glob("*/*.graph"))
    vc_files = list(res_dir.glob("*/*.vertex_cover"))
    matching_files = list(res_dir.glob("*/*.maximal_matching"))

    graph_files = sorted(graph_files, key=lambda x: x.stem)
    vc_files = sorted(vc_files, key=lambda x: x.stem)
    matching_files = sorted(matching_files, key=lambda x: x.stem)

    table_data: list[list] = []

    for i in trange(len(graph_files)):
        data = Data(graph_files[i], matching_files[i], vc_files[i])
        graph = Graph(data.edges, data.nodes)
        graph.calculate_approximate()
        graph.calculate_optimal()

        save_path_output = output_dir.joinpath(f"{graph_files[i].stem}.lpp_approx_cover")
        save_path_img = output_dir_img.joinpath(f"{graph_files[i].stem}.png")

        graph.store(save_path_output)
        visualise(save_path_img, data.nodes, data.edges, graph.solution, graph.solution_approx)

        # n,m     vc size     runtime     approx size     runtime     approx factor
        table_data.append(
            [f"{(data.num_nodes,data.num_edges)}",
             len(graph.solution),
             round(graph.duration * 1e-6, 4),
             len(graph.solution_approx),
             round(graph.duration_approx * 1e-6,4),
             len(graph.solution_approx) / len(graph.solution),
             len(data.matching_vertices) / len(graph.solution)]
        )
    
    table_data = sorted(table_data, key=lambda x: int(x[0].split(",")[1].rstrip(')')))

    with open(res_dir.joinpath("table.csv"), "w") as file:
        writer = csv.writer(file)
        writer.writerows([
            ["", "LP Optimal (Integer Programming)", "", "LPP Approximation","","","Greedy Approximation"],
            ["(n,m)", "Vertex Cover Size", "Runtime (in Seconds)", "Approximate VC Size", "Runtime (in Seconds)",
             "Approximation Factor", "Greedy Approximation Factor"]
        ])
        writer.writerows(table_data)


def main():
    opts = parse_args()

    print("Approximating for graph with 10 vertices")
    node_10 = pth.Path(opts.node10)
    execute_for_res_dir(node_10)

    print("Approximating for graph with 20 vertices")
    node_20 = pth.Path(opts.node20)
    execute_for_res_dir(node_20)




if __name__ == "__main__":
    main()
    # graph = pth.Path("./resources_nodes10/graphs/graph_20.graph")
    # maximal_matching = pth.Path("./resources_nodes10/maximal_matching/graph_20.maximal_matching")
    # vertex = pth.Path("./resources_nodes10/vertex/graph_20.vertex_cover")

    # data = Data(graph, maximal_matching, vertex)
    # graph = Graph(data.edges, data.nodes)
    # graph.calculate_optimal()
    # print(graph.solution)