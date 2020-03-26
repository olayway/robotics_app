<template>
  <div class="registration-panel">
    <v-container class="pa-12">
      <v-card tile class="mx-12">
        <v-row no-gutters>
          <v-col cols="4">
            <v-img height="100%" src="@/assets/images/subscribe_2_alpha.jpg">
              <v-container fill-height pa-7>
                <v-row no-gutters justify-content="center">
                  <v-col>
                    <v-row justify="center">
                      <p>Already have an account?</p>
                    </v-row>
                    <v-row justify="center">
                      <OutlinedButton>Sign In</OutlinedButton>
                    </v-row>
                  </v-col>
                </v-row>
              </v-container>
            </v-img>
          </v-col>

          <v-col cols="8">
            <v-container class="pb-12">
              <v-row no-gutters justify="end">
                <AutoMateLogo fontSize="18px"></AutoMateLogo>
              </v-row>
              <v-row no-gutters class="my-6" justify="center">
                <p class="form-title">Create an account</p>
              </v-row>
              <v-row no-gutters justify="center">
                <v-col cols="10" md="6">
                  <v-form class="d-flex flex-column" ref="form" lazy-validation>
                    <v-text-field v-model="username" label="Username" required></v-text-field>

                    <v-text-field v-model="email" label="E-mail" required></v-text-field>
                    <v-text-field v-model="password" label="Password" required></v-text-field>
                    <v-text-field v-model="password_confirm" label="Confirm password" required></v-text-field>

                    <v-checkbox
                      v-model="agree"
                      :rules="[v => !!v || 'You must agree to continue!']"
                      label="I agree to the collection and processing of personal data by AutoMate."
                      required
                      class="checkbox"
                    ></v-checkbox>

                    <FilledButton class="align-self-center"></FilledButton>
                  </v-form>
                </v-col>
              </v-row>
            </v-container>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import OutlinedButton from '@/components/base/OutlinedButton.vue'
import FilledButton from '@/components/base/FilledButton.vue'
import AutoMateLogo from '@/components/base/AutoMateLogo.vue'
export default {
  name: 'Regsiter',
  components: { OutlinedButton, FilledButton, AutoMateLogo },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password_confirm: '',
      agree: false
    }
  },
  methods: {
    register() {
      this.$store.dispatch('register', {
        username: this.username,
        email: this.email,
        password: this.password,
        agree: this.agree
      })
    }
  }
}
</script>

<style scoped>
.registration-panel {
  background: rgba(20, 18, 40, 0.98);
  font-family: Maven Pro;
  height: 750px;
}

.registration-panel p {
  font-size: 20px;
  color: #fff;
  text-align: center;
}

p.form-title {
  color: rgba(20, 18, 40, 0.98);
}

form >>> label {
  font-size: 14px;
}
.checkbox >>> label {
  font-size: 10px;
  line-height: 14px;
}
</style>>
  
