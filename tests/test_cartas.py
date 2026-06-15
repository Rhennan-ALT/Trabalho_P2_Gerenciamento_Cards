#criar uma carta
def test_criar_cartap(client):
    response = client.post("/cartas",
        json={
        "nome":"Gengar",
        "tipo":"Fantasma",
        "hp": 120,
        "rar": "Holográfica",
        "desc": "Pokémon Favorito hehe"
    }
)
    assert response.status_code == 201
    data = response.json()

    assert data["id"] > 0
    assert data["nome"] == "Gengar"
    assert data["tipo"] == "Fantasma"
    assert data["hp"] == 120
    assert data["rar"] == "Holográfica"
    assert data["desc"] == "Pokémon Favorito hehe"

#get geral
def test_get_cartasp(client):

    client.post("/cartas",
        json={
            "nome": "Gengar",
            "tipo": "Fantasma",
            "hp": 120,
            "rar": "Holográfica",
            "desc": "Pokémon Favorito"
        }
    )

    response = client.get("/cartas")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

    assert data[0]["nome"] == "Gengar"
    assert data[0]["tipo"] == "Fantasma"
    assert data[0]["hp"] == 120

#get com id
def test_get_cartp_id(client):

    created = client.post("/cartas",
        json={
            "nome": "Charizard",
            "tipo": "Fogo",
            "hp": 150,
            "rar": "Ultra Rara",
            "desc": "Dragão de fogo"
        }
    )

    card_id = created.json()["id"]
    response = client.get(f"/cartas/{card_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == card_id
    assert data["nome"] == "Charizard"
    assert data["tipo"] == "Fogo"
    assert data["hp"] == 150
    assert data["rar"] == "Ultra Rara"

#update de uma carta
def test_update_cartap(client):

    created = client.post("/cartas",
        json={
            "nome": "Pikachu",
            "tipo": "Elétrico",
            "hp": 60,
            "rar": "Comum",
            "desc": "Mascote"
        }
    )

    card_id = created.json()["id"]

    response = client.put(f"/cartas/{card_id}",
        json={
            "nome": "Raichu",
            "tipo": "Elétrico",
            "hp": 90,
            "rar": "Rara",
            "desc": "Evolução do Pikachu"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == card_id
    assert data["nome"] == "Raichu"
    assert data["hp"] == 90
    assert data["rar"] == "Rara"
    assert data["desc"] == "Evolução do Pikachu"

#deletar uma carta
def test_delete_cartap(client):

    created = client.post("/cartas",
        json={
            "nome": "Bulbasaur",
            "tipo": "Planta",
            "hp": 70,
            "rar": "Comum",
            "desc": "Inicial de Kanto"
        }
    )

    card_id = created.json()["id"]

    response = client.delete(f"/cartas/{card_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Essa Carta foi Deletada..."
    response = client.get(f"/cartas/{card_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Essa Carta não foi Encontrada..."

#teste de erro
def test_erro_cartap(client):
    response = client.get("/cartas/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Essa Carta não foi Encontrada..."