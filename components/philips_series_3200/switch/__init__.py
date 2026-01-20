diff --git a/components/philips_series_3200/switch/__init__.py b/components/philips_series_3200/switch/__init__.py
index 3333333..4444444 100644
--- a/components/philips_series_3200/switch/__init__.py
+++ b/components/philips_series_3200/switch/__init__.py
@@ -1,24 +1,24 @@
 import esphome.codegen as cg
 import esphome.config_validation as cv
 from esphome.components import switch
 from esphome.const import CONF_ID

 from .. import CONTROLLER_ID, PhilipsSeries3200, philips_series_3200_ns

 DEPENDENCIES = ["philips_series_3200"]

 CLEAN_DURING_START = "clean"

 power_switch_namespace = philips_series_3200_ns.namespace("philips_power_switch")
 PowerSwitch = power_switch_namespace.class_("Power", switch.Switch, cg.Component)

-CONFIG_SCHEMA = switch.SWITCH_SCHEMA.extend(
+CONFIG_SCHEMA = switch.switch_schema(PowerSwitch).extend(
     {
         cv.GenerateID(): cv.declare_id(PowerSwitch),
         cv.Required(CONTROLLER_ID): cv.use_id(PhilipsSeries3200),
         cv.Optional(CLEAN_DURING_START, default=True): cv.boolean,
     }
 ).extend(cv.COMPONENT_SCHEMA)
