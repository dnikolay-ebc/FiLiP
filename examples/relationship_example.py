import logging

from filip.clients.ngsi_v2 import ContextBrokerClient
from filip.models.ngsi_v2.context import ContextEntity
from filip.models.base import FiwareHeader


# Setting up logging
logging.basicConfig(
    level='INFO',
    format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def create_store_entities(fiware_header: FiwareHeader):

    with ContextBrokerClient(fiware_header=fiware_header) as cb_client:
        store_dict = [{"type": "Store",
                       "id": "urn:ngsi-ld:Store:001",
                       "address": {
                           "type": "Text",
                           "value": "Bornholmer Straße 65"
                       },
                       "location": {
                           "type": "Text",
                           "value": "[13.3986, 52.5547]"
                       },
                       "name": {
                           "type": "Text",
                           "value": "Bösebrücke Einkauf"
                       }},
                      {
                          "type": "Store",
                          "id": "urn:ngsi-ld:Store:002",
                          "address": {
                              "type": "Text",
                              "value": "Friedrichstraße 44"
                          },
                          "location": {
                              "type": "Text",
                              "value": "[13.3903, 52.5075]"
                          },
                          "name": {
                              "type": "Text",
                              "value": "Checkpoint Markt"
                          }
                      }]
        store_entities = []
        for store in store_dict:
            cb_client.post_entity(ContextEntity(**store))
            store_entities.append(ContextEntity(**store))
        return store_entities


def create_product_entities(fiware_header: FiwareHeader):
    with ContextBrokerClient(fiware_header=fiware_header) as cb_client:
        product_dict = [
            {
                "id": "urn:ngsi-ld:Product:001", "type": "Product",
                "name": {
                    "type": "Text", "value": "Beer"
                },
                "size": {
                    "type": "Text", "value": "S"
                },
                "price": {
                    "type": "Integer", "value": 99
                }
            },
            {
                "id": "urn:ngsi-ld:Product:002", "type": "Product",
                "name": {
                    "type": "Text", "value": "Red Wine"
                },
                "size": {
                    "type": "Text", "value": "M"
                },
                "price": {
                    "type": "Integer", "value": 1099
                }
            },
            {
                "id": "urn:ngsi-ld:Product:003", "type": "Product",
                "name": {
                    "type": "Text", "value": "White Wine"
                },
                "size": {
                    "type": "Text", "value": "M"
                },
                "price": {
                    "type": "Integer", "value": 1499
                }
            },
            {
                "id": "urn:ngsi-ld:Product:004", "type": "Product",
                "name": {
                    "type": "Text", "value": "Vodka"
                },
                "size": {
                    "type": "Text", "value": "XL"
                },
                "price": {
                    "type": "Integer", "value": 5000
                }
            }
        ]
        product_entities = []
        for product_entity in product_dict:
            cb_client.post_entity(ContextEntity(**product_entity))
            product_entities.append(ContextEntity(**product_entity))
        return product_entities


def create_inventory(fiware_header: FiwareHeader):

    with ContextBrokerClient(fiware_header=fiware_header) as cb_client:
        inventory_dict = {
            "id": "urn:ngsi-ld:InventoryItem:001", "type": "InventoryItem",
            "refStore": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Store:001"
            },
            "refProduct": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Product:001"
            },
            "stockCount": {
                "type": "Integer", "value": 10000
            }}
        inventory_entity = ContextEntity(**inventory_dict)
        cb_client.post_entity(inventory_entity)
        return inventory_entity


def delete_entities(fiware_header: FiwareHeader, entities_to_delete):
    with ContextBrokerClient(fiware_header=fiware_header) as cb_client:
        for entity in entities_to_delete:
            cb_client.delete_entity(entity_id=entity.id)
        return


def get_entities(fiware_header: FiwareHeader, query: str):
    with ContextBrokerClient(fiware_header=fiware_header) as cb_client:
        logger.info(cb_client.get_entity_list(q=query))


if __name__ == "__main__":
    fiware_header = FiwareHeader(service='filip', service_path='/testing')

    example_store_entities = create_store_entities(
        fiware_header=fiware_header)
    example_product_entities = create_product_entities(
        fiware_header=fiware_header)
    example_inventory_entity = create_inventory(
        fiware_header=fiware_header)

    logger.info("------Inventory relationship with Store and Product------")
    logger.info(example_inventory_entity.get_relationships())

    logger.info("------It should return the inventory item according to the "
                "relationship------")
    get_entities(fiware_header=fiware_header,
                 query="refProduct==urn:ngsi-ld:Product:001")
    get_entities(fiware_header=fiware_header,
                 query="refStore==urn:ngsi-ld:Store:001")

    logger.info("------It should not return the inventory item according to the "
                "relationship------")
    get_entities(fiware_header=fiware_header,
                 query="refStore==urn:ngsi-ld:Store:002")

    logger.info("------Deleting all test entities------")
    delete_entities(fiware_header=fiware_header,
                    entities_to_delete=example_store_entities)
    delete_entities(fiware_header=fiware_header,
                    entities_to_delete=example_product_entities)
    delete_entities(fiware_header=fiware_header,
                    entities_to_delete=[example_inventory_entity])
