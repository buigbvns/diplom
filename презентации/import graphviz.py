import graphviz

def generate_training_graphviz_updated():
    """
    Generates a Graphviz DOT representation of the updated training flowchart.
    """

    dot = graphviz.Digraph(comment='Обучение SLAM', graph_attr={'rankdir': 'TB'})

    # Nodes
    dot.node('A', 'Начало:\nСтудент с\nнулевым опытом', shape='oval', style='filled', fillcolor='#a8e6cf')
    dot.node('B', 'Модуль 1:\nОсновы Linux &\nКомандная строка', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('C', 'Модуль 2:\nВведение в ROS', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('D', 'Модуль 3:\nУправление роботом\nв ROS', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('E', 'Модуль 4:\nОсновы\nSLAM-навигации', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('F', 'Модуль 5:\nSLAM & Navigation\nStack', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('G', 'Модуль 6:\nGmapping &\nРучное\nуправление', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('H', 'Модуль 7:\nАвтономная\nнавигация в лабиринте', shape='box', style='filled', fillcolor='#dcedc1')
    dot.node('I', 'Конец:\nРобот автономно\nв лабиринте', shape='oval', style='filled', fillcolor='#a8e6cf')

    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')

    # Sub-nodes (optional, for more detail) - Add these as needed for clarity

    return dot

if __name__ == "__main__":
    try:
        graph = generate_training_graphviz_updated()
        graph.render('training_flowchart_updated', view=True, format='png')
        print("Flowchart generated successfully as training_flowchart_updated.png")
    except graphviz.backend.ExecutableNotFound as e:
        print(f"Error: Graphviz executable not found. Please install Graphviz system-wide.\n{e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")