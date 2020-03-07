<template>
  <v-card class="filter-card pa-5 ma-2" dark color="#293453">
    <v-container pa-0>
      <v-row no-gutters class="mb-3">
        <v-col cols="6" class="d-flex">
          <img src="@/assets/images/card_img.jpg" alt="yaskawa_img" />
        </v-col>
        <v-col cols="6" class="pl-3 d-flex flex-column justify-space-between">
          <div class="card-titles">
            <p style="text-align: bottom" class="card-title-1">YASKAWA</p>
            <p class="card-title-2">MOTOMAN SDA20D</p>
            <p class="card-title-3">Dual-Arm Industrial Robot</p>
          </div>
          <div class="divider"></div>
          <div>
            <p class="company">
              IRA – Industrial Robot Automation Aps, Dänemark
            </p>
            <p class="applications">
              Assembly | Machine Tending | Part Transfer | Press/Forming
            </p>
          </div>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="d-flex justify-start">
          <p class="short-descr">
            Complete the production automation cycle in Avícola El Ángel and
            optimise the final handling process
          </p>
        </v-col>
        <v-col class="d-flex shrink ml-3 justify-end">
          <v-btn class="more-button" outlined rounded color="#F1D302"
            >More Info</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'FilterCard',
  data() {
    return {}
  }
}
</script>

<style scoped>
img {
  width: 100%;
  height: auto;
}

.filter-card * {
  border: 1px solid white;
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
}

.card-titles * {
  margin: 0;
}

p.short-descr {
  font-size: 14px;
  color: #c4c4c4;
  display: inline-block;
  margin: 0;
}

.card-title-1 {
  font-size: 24px;
  /* line-height: initial */
}

.card-title-2 {
  font-size: 18px;
}

.card-title-3 {
  font-size: 16px;
  color: #f1d302;
}

.divider {
  border-bottom: 1px solid white;
  width: 15%;
}

.company,
.applications {
  font-size: 12px;
  margin: 0;
}

.company {
  font-weight: bold;
}

.more-button {
  font-size: 14px;
}
</style>
