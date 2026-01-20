 import esphome.codegen as cg
 import esphome.config_validation as cv
 from esphome.components import text_sensor
 from esphome.const import CONF_ID

 from .. import CONTROLLER_ID, PhilipsSeries3200, philips_series_3200_ns

 USE_LATTE = "use_latte"
 STATUS_SENSOR_ID = "status_sensor_id"

 philips_status_sensor_ns = philips_series_3200_ns.namespace("philips_status_sensor")
 StatusSensor = philips_status_sensor_ns.class_(
     "StatusSensor", text_sensor.TextSensor, cg.Component
 )

-CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend(
+CONFIG_SCHEMA = text_sensor.text_sensor_schema(StatusSensor).extend(
     {
         cv.GenerateID(): cv.declare_id(StatusSensor),
         cv.Required(CONTROLLER_ID): cv.use_id(PhilipsSeries3200),
         cv.Optional(USE_LATTE, default=False): cv.boolean,
     }
 ).extend(cv.COMPONENT_SCHEMA)
