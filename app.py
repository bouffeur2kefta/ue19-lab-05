import requests
import sys

def get_random_joke():
    """Récupère une blague aléatoire depuis l'API JokesAPI"""
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke', timeout=10)
        response.raise_for_status()
        
        joke_data = response.json()
        print(f"\n{joke_data['setup']}")
        print(f"{joke_data['punchline']}\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API : {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Erreur de format de réponse : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_random_joke()
