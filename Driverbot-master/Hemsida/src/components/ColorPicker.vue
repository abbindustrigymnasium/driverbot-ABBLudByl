<template>
  <v-container class="container">
    <v-row align-center justify-center>
      <v-col>
        <div>
          <v-btn large class="headline" color="success" @click="send('F')">Forward</v-btn>
        </div>
        <div>
          <v-btn large class="headline" color="success" @click="send('L')">Left</v-btn>
          <v-btn large class="headline" color="success" @click="send('S')">Stop</v-btn>
          <v-btn large class="headline" color="success" @click="send('R')">Right</v-btn>
        </div>
        <div>
          <v-btn large class="headline" color="success" @click="send('B')">Backward</v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
var mqtt = require("mqtt"),
  /* eslint-disable */
  url = require("url");

export default {
  created() {
    this.connect();
  },
  data: () => ({
    connected: false,
    client: "1032985790821357t08792345098123570892357809832157",
    user: "ludvig.bylund@abbindustrigymnasium.se",
    pass: "qazwsxedcrfvtgb"
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
      this.client.publish(
        "ludvig.bylund@abbindustrigymnasium.se/test",
        message
      );
    }
  }
};
</script>
<style>
.container {
  padding: 17%;
}
</style>