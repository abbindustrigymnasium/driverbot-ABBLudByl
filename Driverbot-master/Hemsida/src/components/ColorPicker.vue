<template>
  <div>
    <v-col cols="12">
    </v-col>
      <v-btn @click="send('f')"> Forward </v-btn>
    <!-- <v-col cols="12">
      <v-slider v-model="color.saturation" min="0" max="100" label="Saturation"></v-slider>
    </v-col>-->
    <v-col cols="12">
    </v-col>
  </div>
</template>

<script>
var mqtt = require("mqtt"),
/* eslint-disable */
  url = require("url");

export default {
  created() {
    this.connect();
    this.send("FishPog");
  },
  data: () => ({
    connected: false,
    client: "1032985790821357t08792345098123570892357809832157",
    user: "ludvig.bylund@abbindustrigymnasium.se",
    pass: "qazwsxedcrfvtgb",
  }),
  methods: {
        connect() {
      var mqtt_url = "maqiatto.com";
      var url = "mqtt://" + mqtt_url;
      var options = {
        port: 8883,
        clientId:
          "mqttjs_" +
          Math.random()
            .toString(16)
            .substr(2, 8),
        username: this.user,
        password: this.pass
      };
      // user = this.options.username
      // pass = this.options.password
      /* eslint-disable */
      console.log("connecting");
      this.client = mqtt.connect(url, options);
      /* eslint-disable */
      console.log("connected?");
      this.client
        .on("error", function(error) {
          /* eslint-disable */
          console.log("no");
          this.connected = false;
          /* eslint-disable */
          console.log(this.Alert, this.connected);
        })
        .on("close", function(error) {
          /* eslint-disable */
          console.log("no");
          this.connected = false;
        });
      this.connected = true;
    },
    send(message) {
      this.client.publish("ludvig.bylund@abbindustrigymnasium.se/test", message);
    }

  },

};
</script>