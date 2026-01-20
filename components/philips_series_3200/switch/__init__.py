import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import CONF_ID

from .. import CONTROLLER_ID, PhilipsSeries3200, philips_series_3200_ns

DEPENDENCIES = ["philips_series_3200"]

CLEAN_DURING_START = "clean"

power_switch_namespace = philips_series_3200_ns.namespace("philips_power_switch")
PowerSwitch = power_switch_namespace.class_("Power", switch.Switch, cg.Component)

CONFIG_SCHEMA = switch.switch_schema(PowerSwitch).extend(
    {
        cv.GenerateID(): cv.declare_id(PowerSwitch),
        cv.Required(CONTROLLER_ID): cv.use_id(PhilipsSeries3200),
        cv.Optional(CLEAN_DURING_START, default=True): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    controller = await cg.get_variable(config[CONTROLLER_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await switch.register_switch(var, config)

    cg.add(var.set_cleaning(config[CLEAN_DURING_START]))
    cg.add(controller.register_power_switch(var))
