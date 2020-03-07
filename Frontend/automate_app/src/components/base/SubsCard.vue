<template>
  <v-parallax src="@/assets/images/subscribe_2_alpha.jpg" style="height: auto">
    <v-container class="subscribe-form py-10">
      <v-row class="justify-space-around px-10">
        <v-col cols="10" md="5" class="d-flex flex-column">
          <p class="subs-title">Subscribe now for new use cases</p>
          <div class="divider"></div>
          <p class="subs-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean urna
            at nibh nisi volutpat tincidunt viverra.
          </p>
        </v-col>
        <v-col cols="10" md="5" class="d-flex flex-column align-center">
          <v-text-field
            hide-details
            rounded
            validate-on-blur
            class="subs-field"
            :placeholder="placeholder"
            clear-icon="mdi-close-circle"
            clearable
            outlined
            dense
            type="text"
            single-line
            dark
          ></v-text-field>
          <p class="subs-terms">
            By submitting this form, I confirm that I agree to the collection
            and processing of personal data by Adjust, as further described in
            the Privacy Policy.
          </p>
          <v-btn class="subs-btn" rounded>Let's Go!</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-parallax>
</template>

<script>
export default {
  name: 'SubsCard',
  data() {
    return {
      placeholder: 'Enter your email here...'
      //   rules: {
      //     email: value => {
      //       const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      //       return pattern.test(value) || 'Invalid e-mail.'
      //     }
      //   }
    }
  }
}
</script>

<style scoped>
.subscribe-form * {
  /* border: 1px solid white; */
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
}

.subs-title {
  font-size: 24px;
}

.subs-text {
  font-size: 18px;
}

.subs-terms {
  font-size: 11px;
  text-align: center;
}

.subscribe-form p,
.subscribe-form div,
.subs-field,
.subs-btn {
  margin: 10px 0;
}

/* .subscribe-form p.subs-terms {
  margin-top: 0px;
} */

.divider {
  border-bottom: 1px solid white;
  width: 54px;
}

.subs-btn {
  text-transform: initial;
  font-size: 16px;
  letter-spacing: 0;
}

.subs-field {
  width: 75%;
}
</style>
