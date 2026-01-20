diff --git a/components/philips_series_3200/button/__init__.py b/components/philips_series_3200/button/__init__.py
index 7777777..8888888 100644
--- a/components/philips_series_3200/button/__init__.py
+++ b/components/philips_series_3200/button/__init__.py
@@ -43,7 +43,7 @@ def validate_long_press(config):
 
 
 CONFIG_SCHEMA = cv.All(
-    button.BUTTON_SCHEMA.extend(
+    button.button_schema(ActionButton).extend(
         {
             cv.GenerateID(): cv.declare_id(ActionButton),
             cv.Required(CONTROLLER_ID): cv.use_id(PhilipsSeries3200),
             cv.Required(CONF_ACTION): cv.enum(ACTIONS, upper=True, space="_"),
             cv.Optional(CONF_LONG_PRESS, default=False): cv.boolean,
         },
     ).extend(cv.COMPONENT_SCHEMA),
     validate_long_press,
 )
