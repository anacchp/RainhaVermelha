<template>
  <v-container class="fill-height justify-center">
    <v-responsive class="align-center text-center fill-height">

      <v-sheet :height="700" :width="1200" color="pink-lighten-4">
        <v-row>
          <v-col cols="6">
            <v-col class="mx-auto pl-14 pt-10 pb-8" theme="dark" max-width="400">
              <h1 class="title text-h2 text-left font-weight-bold">Descubra as jóias escondidas da literatura</h1>
            </v-col>
            <v-col class="mx-auto px-14" theme="dark" max-width="400">
              <p class="text text-h5 text-left">
                Desbloqueie o poder dos livros com o Book Graph. A nossa plataforma utiliza algoritmos avançados para
                extrair informações valiosas dos livros.
              </p>
            </v-col>
            <v-col cols="auto pa-10">
              <v-row justify="center" class="d-flex">
                <v-col>
                  <v-autocomplete rounded variant="solo-filled" label="Busque o livro"
                    placeholder="Rainha Vermelha" v-model="values" :items="items"></v-autocomplete>
                </v-col>
                <v-col cols="auto">
                  <v-btn rounded variant="elevated" class="dark" size="x-large" color="purple-darken-4"
                    prepend-icon="mdi-magnify" @click="goTo()">Buscar</v-btn>
                </v-col>

              </v-row>
            </v-col>
          </v-col>

          <v-col cols="6">
            <img src="../assets/girl_book.jpg">
          </v-col>
        </v-row>
      </v-sheet>


    </v-responsive>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      items: ['Rainha Vermelha', 'Harry Potter'],
      values: '',
    }),
    methods: {
      goTo() {
        this.$router.push('/book')
      }
    }
  }
</script>

<style>
.title{
  font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji !important;
  line-height: 1.4;
}
.text{
  font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji !important;
}


</style>
