<template>
    <v-parallax src="../assets/capa.jpg">
        <div class="d-flex flex-column fill-height justify-center align-center text-white">
            <v-sheet height="100" :elevation="20" color="grey-lighten-2" rounded>
                <h1 class="text-h1 font-weight-thin mb-4">
                    Rainha Vermelha
                </h1>
            </v-sheet>
        </div>
    </v-parallax>

    <v-container>
        <div class="py-15">
            <p class="text-snopse">Sinopse</p>
            <p class="text"> O mundo de Mare Barrow é dividido pelo sangue: vermelho ou prateado. Mare e sua família são vermelhos: plebeus, humildes, destinados a servir uma elite prateada cujos poderes sobrenaturais os tornam quase deuses. Mare rouba o que pode para ajudar sua família a sobreviver e não tem esperanças de escapar do vilarejo miserável onde mora. Entretanto, numa reviravolta do destino, ela consegue um emprego no palácio real, onde, em frente ao rei e a toda a nobreza, descobre que tem um poder misterioso... Mas como isso seria possível, se seu sangue é vermelho? Em meio às intrigas dos nobres prateados, as ações da garota vão desencadear uma dança violenta e fatal, que colocará príncipe contra príncipe - e Mare contra seu próprio coração.</p>
        </div>
    </v-container>
    
  <v-container class="pt-10">
      <div>
        <p class="text-snopse pb-5">Perguntas</p>
        <v-text-field
          variant="outlined"
          label="Faça uma pergunta sobre o livro"
          disabled=""
          ></v-text-field>
        <v-expansion-panels class="mb-6">
          <v-expansion-panel v-for="i in pokemons" :key="i">
            <v-expansion-panel-title expand-icon="mdi-menu-down">
              {{ i.question }} 
            </v-expansion-panel-title>
            <v-expansion-panel-text v-for="j in i.answer" :key="j"
              >
              {{ j }}
              </v-expansion-panel-text
            >
          </v-expansion-panel>
        </v-expansion-panels>
      </div>

  </v-container>
</template>
<script>
import axios from 'axios'
export default {
    data: () => ({
      questions: [],
      answer: [],
      pokemons: []
    }),
    created: 
        function(){
            axios.get("http://localhost:5000/questions").then(res =>{
            this.pokemons = res.data;
            })
        }
    }
</script>

<style>
.text-snopse{
  font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji !important;
  font-size: 5rem;
}
</style>