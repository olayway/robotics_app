<template>
  <v-card min-height="800px" class="registration-panel py-6" flat tile>
    <v-container fluid fill-height class="pa-12">
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card tile class="mx-12">
            <v-row no-gutters>
              <v-col cols="4">
                <v-img
                  height="100%"
                  src="@/assets/images/subscribe_2_alpha.jpg"
                >
                  <v-container fill-height pa-7>
                    <v-row no-gutters justify-content="center">
                      <v-col>
                        <v-row justify="center">
                          <p>New to AutoMate?</p>
                        </v-row>
                        <v-row justify="center">
                          <router-link to="/register" class="register-button">
                            <OutlinedButton>Register</OutlinedButton>
                          </router-link>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-img>
              </v-col>

              <v-col cols="8">
                <v-container class="pb-12">
                  <v-row no-gutters justify="end">
                    <AutoMateLogo font-size="18px"></AutoMateLogo>
                  </v-row>
                  <v-row no-gutters class="my-6" justify="center">
                    <p class="form-title">Welcome back !</p>
                  </v-row>
                  <v-row no-gutters justify="center">
                    <v-col cols="10" md="6">
                      <v-form
                        ref="form"
                        v-model="form_valid"
                        class="d-flex flex-column"
                        lazy-validation
                      >
                        <v-text-field
                          v-model="username"
                          label="Username"
                          required
                          @keydown.enter="login"
                        ></v-text-field>

                        <v-text-field
                          v-model="password"
                          label="Password"
                          required
                          :type="showPassword ? 'text' : 'password'"
                          :append-icon="
                            showPassword ? 'mdi-eye' : 'mdi-eye-off'
                          "
                          @click:append="showPassword = !showPassword"
                          @keydown.enter="login"
                        ></v-text-field>
                        <v-btn
                          class="btn align-self-center"
                          depressed
                          color="rgba(20, 18, 40, 0.98)"
                          dark
                          rounded
                          @click="login"
                          >Let's Go!</v-btn
                        >
                        <!-- <FilledButton class="align-self-center" @click="authenticate"></FilledButton> -->
                      </v-form>
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import OutlinedButton from '@/components/base/OutlinedButton.vue'
// import FilledButton from '@/components/base/FilledButton.vue'
import AutoMateLogo from '@/components/base/AutoMateLogo.vue'
export default {
  name: 'Login',
  components: { OutlinedButton, AutoMateLogo },
  data() {
    return {
      username: '',
      password: '',
      form_valid: true,
      errorMsg: '',
      showPassword: false
    }
  },
  methods: {
    login() {
      const { username, password } = this
      this.$store
        .dispatch('login', { username, password })
        .then(() => this.$router.push('/user-panel'))
        .catch(error => console.log(error))
    }
  }
}
</script>

<style scoped>
.registration-panel {
  background: rgba(20, 18, 40, 0.98);
  font-family: Maven Pro;
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

.btn {
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
  text-transform: initial;
  font-size: 16px;
  letter-spacing: 0;
  margin: 10px 0;
}

.register-button {
  text-decoration: none;
}
</style>
