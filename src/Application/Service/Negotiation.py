from src.Application.Entities.Negotiation import Negotiation
from src.Application.Entities.Promotion import PromotionNegotiation

from src.Application.DTO.Request.Negotiation import NegotiationRequestDTO
from src.Application.DTO.Request.TypeValidator import RequestTypeValidator
from src.Application.DTO.Response.ProfitsAndLooses import ProfitsAndLoosesResponseDTO

from src.Application.Exceptions.ApplicationException import ApplicationException


def negotiation_service(request_json):
    try:
        RequestTypeValidator(
            NegotiationRequestDTO, 
            request_json
        )
        negotiation: Negotiation = Negotiation(
            **NegotiationRequestDTO(
                **request_json
            ).__dict__
        )
        profits_and_looses_response: dict = ProfitsAndLoosesResponseDTO(
            negotiation.monthly_profits_and_looses, negotiation.price_offer_is_higher_than_minimum
        ).__dict__
        return profits_and_looses_response
    except Exception as e:
        raise ApplicationException(e)

