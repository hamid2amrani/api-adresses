import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer

class AddressCreateView(APIView):
    def post(self, request):
        q = request.data.get("q", "").strip()
        if not q:
            return Response(
                {"error": "Le champ 'q' est requis et doit être une chaîne non vide."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            res = requests.get(f"https://api-adresse.data.gouv.fr/search/?q={q}&limit=1", timeout=5)
            data = res.json()
        except Exception:
            return Response(
                {"error": "Erreur serveur : impossible de contacter l'API externe."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if not data["features"]:
            return Response(
                {"error": "Adresse non trouvée. Aucun résultat ne correspond à votre recherche."},
                status=status.HTTP_404_NOT_FOUND
            )

        props = data["features"][0]["properties"]
        geometry = data["features"][0]["geometry"]["coordinates"]

        address = Address.objects.create(
            label=props.get("label"),
            housenumber=props.get("housenumber", ""),
            street=props.get("street", ""),
            postcode=props.get("postcode", ""),
            citycode=props.get("citycode", ""),
            latitude=geometry[1],
            longitude=geometry[0],
        )
        return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)


class RiskCheckView(APIView):
    def get(self, request, id):
        try:
            address = Address.objects.get(pk=id)
        except Address.DoesNotExist:
            return Response(
                {"error": "Adresse non trouvée."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            lon, lat = address.longitude, address.latitude
            res = requests.get(
                f"https://www.georisques.gouv.fr/api/v1/resultats_rapport_risque?latlon={lon},{lat}",
                timeout=10
            )
            return Response(res.json(), status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"error": "Erreur serveur : échec de la récupération des données de Géorisques."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

