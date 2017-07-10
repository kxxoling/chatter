<template lang="jade">
.index
  .random-room
    input.random(type="input", v-model=input, placeholder="Input something within 16 characters.")
    button.go(@click="go") GO!
</template>

<script>
const randomRoomLabels = [
  'FinalFlightOfTheOsiris',
  'SecondRenaissance',
  'KidsStory',
  'Program',
  'WorldRecord',
  'Beyond',
  'ADetectiveStory',
  'Matriculated',
];

export default {
  data() {
    return {
      input: '',
    };
  },
  methods: {
    go() {
      let label;
      if (!this.input) {
        label = randomRoomLabels[Math.floor(Math.random() * randomRoomLabels.length)];
        this.input = label;
      }
      this.$router.push({ name: 'room', params: { label } });
    },
  },
};
</script>

<style lang="stylus" scoped>
.index
  display flex
  justify-content center
  background black
  height 100vh

  .random-room
    padding-top 10rem
    height 3rem

    input
      font-size 1.25rem
      padding 1rem
      width 24rem
      height 100%
      box-sizing border-box

    .go
      height 100%
      width 4rem
      border none
      background #44c
      color white
      cursor pointer
</style>
