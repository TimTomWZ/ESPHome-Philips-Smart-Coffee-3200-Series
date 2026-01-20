diff --git a/components/philips_series_3200/number/__init__.py b/components/philips_series_3200/number/__init__.py
index 5555555..6666666 100644
--- a/components/philips_series_3200/number/__init__.py
+++ b/components/philips_series_3200/number/__init__.py
@@ -1,6 +1,6 @@
 import esphome.codegen as cg
 import esphome.config_validation as cv
 from esphome.components import number
 from esphome.const import CONF_MODE, CONF_TYPE

@@ -45,6 +45,7 @@ TYPES = {
     "SIZE": Type.SIZE,
     "MILK": Type.MILK,
 }
+
 def validate_enum(config):
     """Validate that sources are only used on valid types."""
     if config[CONF_TYPE] == CONF_TYPE_BEAN and config[CONF_SOURCE] == "HOT_WATER":
@@ -55,8 +56,8 @@ def validate_enum(config):
 
 
 CONFIG_SCHEMA = cv.Any(
-    number.NUMBER_SCHEMA.extend(
+    number.number_schema(BeverageSettings).extend(
         {
             cv.GenerateID(): cv.declare_id(BeverageSettings),
             cv.Required(CONTROLLER_ID): cv.use_id(PhilipsSeries3200),
             cv.Required(STATUS_SENSOR_ID): cv.use_id(StatusSensor),
             cv.Required(CONF_TYPE): cv.enum(TYPES, upper=True, space="_"),
             cv.Optional(CONF_MODE, default="SLIDER"): cv.enum(
                 number.NUMBER_MODES, upper=True
             ),
             cv.Optional(CONF_SOURCE, default="ANY"): cv.enum(
                 SOURCES, upper=True, space="_"
             ),
         }
     ).extend(cv.COMPONENT_SCHEMA),
     validate_enum,
 )
