import networkx as netx
import pathlib as pth
from matplotlib import pyplot as plt, patches

def visualise(
            img_save_path: pth.Path,
            graph_nodes: set[int],
            graph_edges: set[tuple[int,int]],
            graph_opt_vertex_cover: set[int],
            graph_approx_vertex_cover: set[int]
        ):
    graph = netx.Graph()

    nodes_list = list(graph_nodes)

    graph.add_nodes_from(nodes_list)
    graph.add_edges_from(graph_edges)

    fig, ax = plt.subplots(1,2, figsize=(22,10))

    optimal_colour = ["orange" if x in graph_opt_vertex_cover else "blue" for x in nodes_list]
    approx_colour = ["red" if x in graph_approx_vertex_cover else "blue" for x in nodes_list]

    optimal_legend_patch = patches.Patch(color="orange", label="Optimal Vertex Cover")
    approx_legend_patch = patches.Patch(color="red", label="Approximate Vertex Cover")

    layout = netx.spring_layout(graph)

    ax[0].set_title("Graph with Optimal Vertex cover")
    netx.draw_networkx_nodes(graph, layout, node_color=optimal_colour, ax=ax[0])
    netx.draw_networkx_edges(graph, layout, edge_color="gray", alpha=0.8, ax=ax[0])

    ax[1].set_title("Graph with Approximate Vertex cover")
    netx.draw_networkx_nodes(graph, layout, node_color=approx_colour, ax=ax[1])
    netx.draw_networkx_edges(graph, layout, edge_color="gray", alpha=0.8, ax=ax[1])

    fig.legend(
        handles=[optimal_legend_patch, approx_legend_patch]
    )

    fig.tight_layout()
    fig.subplots_adjust(top=0.95)

    fig.savefig(img_save_path)
    plt.close(fig)