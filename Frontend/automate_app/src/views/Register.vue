<template>
  <v-card min-height="800px" class="registration-panel" flat tile>
    <v-container class="pa-12">
      <v-row justify="center">
        <v-col cols="12" md="10">
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
                          <p>Already have an account?</p>
                        </v-row>
                        <v-row justify="center">
                          <router-link to="/login" class="login-button">
                            <OutlinedButton>Sign In</OutlinedButton>
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
                    <p class="form-title">Create an account</p>
                  </v-row>
                  <v-row no-gutters justify="center">
                    <v-col cols="10" md="6">
                      <v-form
                        ref="form"
                        v-model="valid"
                        class="d-flex flex-column"
                      >
                        <v-text-field
                          v-model="username"
                          :counter="10"
                          :rules="[rules.name_char, rules.name_len]"
                          label="Username"
                          required
                        ></v-text-field>

                        <v-text-field
                          v-model="email"
                          :rules="[rules.email]"
                          label="E-mail"
                          required
                        ></v-text-field>
                        <v-text-field
                          v-model="company_name"
                          label="Company name"
                          required
                        ></v-text-field>
                        <v-text-field
                          v-model="password"
                          :rules="[rules.password_char, rules.password_len]"
                          label="Password"
                          required
                          :type="showPassword ? 'text' : 'password'"
                          :append-icon="
                            showPassword ? 'mdi-eye' : 'mdi-eye-off'
                          "
                          @click:append="showPassword = !showPassword"
                        ></v-text-field>
                        <v-text-field
                          label="Confirm password"
                          :rules="
                            [v => v === password] || 'Passwords must match'
                          "
                          required
                          :type="showConfirm ? 'text' : 'password'"
                          :append-icon="showConfirm ? 'mdi-eye' : 'mdi-eye-off'"
                          @click:append="showConfirm = !showConfirm"
                        ></v-text-field>

                        <v-checkbox
                          v-model="agree"
                          :rules="[v => !!v || 'You must agree to continue!']"
                          label="I agree to the collection and processing of personal data by AutoMate."
                          required
                          class="checkbox"
                        ></v-checkbox>
                        <v-btn
                          class="btn align-self-center"
                          depressed
                          color="rgba(20, 18, 40, 0.98)"
                          dark
                          rounded
                          @click="register"
                          >Let's Go!</v-btn
                        >
                        <!-- <FilledButton class="align-self-center"></FilledButton> -->
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
  name: 'Register',
  components: { OutlinedButton, AutoMateLogo },
  data() {
    return {
      valid: false,
      username: '',
      email: '',
      company_name: '',
      password: '',
      agree: false,
      showPassword: false,
      showConfirm: false,
      rules: {
        name_char: v =>
          /^.*(?=.*\d)(?=.*[a-zA-Z]).*$/.test(v) ||
          'Username must contain at least one letter and one digit',
        name_len: v =>
          v.length <= 10 || 'Username must be less than 10 characters',
        email: v => /.+@.+\..+/.test(v) || 'Invalid email',
        password_char: v =>
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])/.test(v) ||
          'Password must contain at least 1 lowercase letter, 1 uppercase letter and a special character',
        password_len: v =>
          /(?=.{8,})/.test(v) || 'Password must be at least 8 characters.'
      }
    }
  },
  methods: {
    register() {
      if (this.valid) {
        this.$store
          .dispatch('register', {
            username: this.username,
            company_name: this.company_name,
            email: this.email,
            password: this.password
          })
          .then(() => this.$router.push('/user-panel'))
      }
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

.btn {
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
  text-transform: initial;
  font-size: 16px;
  letter-spacing: 0;
  margin: 10px 0;
}

.login-button {
  text-decoration: none;
}
</style>
