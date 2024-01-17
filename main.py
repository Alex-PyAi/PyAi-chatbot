from sklearn.feature_extraction.text import TfidfVectorizer

class Search:
    def __init__(self, data_dict):
        """Initialise la classe avec le dictionnaire de données."""
        self.data_dict = data_dict
        self.vectorizer = TfidfVectorizer()
        self.vectorized_data = self.vectorize_data()

    def vectorize_data(self):
        """
        Transforme les données du dictionnaire en représentation vectorielle
        pour la recherche vectorielle en utilisant le TF-IDF.
        """
        self.vectorizer()
        return vectorized_data

    def search(self, query_text, top_k=5):
        """
        Effectue une recherche vectorielle sur le dictionnaire de données
        en utilisant la similarité cosinus pour identifier les séries pertinentes.

        :param query_text: Le texte de la requête de l'utilisateur.
        :param top_k: Le nombre de séries les plus pertinentes à retourner.
        :return: Une liste des identifiants des séries les plus pertinentes.
        """
        # Vectorisez la requête de l'utilisateur
        query_vector = self.vectorizer.transform([query_text])

        # Calculez la similarité cosinus entre le vecteur de requête et les vecteurs des séries
        similarities = cosine_similarity(query_vector, self.vectorized_data).flatten()

        # Triez les indices des séries en fonction de leur similarité
        sorted_indices = np.argsort(similarities)[::-1]

        # Sélectionnez les top_k séries les plus pertinentes
        top_k_series = [list(self.data_dict.keys())[index] for index in sorted_indices[:top_k]]

        return top_k_series

# Download series from API 
class Download:
    def __init__(self, api_url):
        """Initialise la classe avec l'URL de l'API."""
        self.api_url = api_url

    def download(self, series_ids):
        """
        Permet de télécharger les séries identifiées grâce à la classe SearchDB
        depuis une API publique (exemple INSEE).
        """
        # Logique de téléchargement depuis l'API ici
        return json_data

# Load JSON inside LLM
class Train:
    def __init__(self, model):
        """Initialise la classe avec le modèle."""
        self.model = model

    def train(self, json_data):
        """
        Permet d'ajouter les données dans le prompt afin d'optimiser la requête.
        """
        # Logique d'ajout des données au modèle ici
        return trained_model

# Chatbox
class Chat:
    def __init__(self, model):
        """Initialise la classe avec le modèle."""
        self.model = model

    def chat(self, message):
        """
        Permet d'interagir avec un LLM sur les données JSON importées.
        Output doit ressembler à une analyse de données avec contexte, évolution, graphiques, tableaux, ...
        """
        # Logique d'interaction avec le modèle et génération de la réponse
        return response

  
 

