import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use('Agg')

def get_graph() : 
    # Sauvegarde en mémoire
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    # print(image_png)
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    
    return graph

def get_plot(x, y):
    
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 4))
    plt.title('Scores des patients')
    plt.xlabel('Nom')
    plt.ylabel('Score')
    plt.bar(x, y, color='skyblue')
    plt.grid(True)
    plt.tight_layout()
    graph = get_graph()

    return graph
 

def plot_scores_as_base64 (scores):
    plt.figure(figsize=(6, 4))
    
    plt.title('Scores du patient')
    plt.xlabel('Scores')
    plt.ylabel('Valeur')
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarde en mémoire
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close()
    return image_base64