
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
