<template>
  <div class="addcard-box" :class="{ '-showerror': error }">
    <div class="form-box">
      <label>
        <input
          @keypress.enter="addCard"
          v-model="passage"
          :class="{ '-error': error }"
          type="text"
          class="input"
          placeholder="Enter Passage"
        />
      </label>
      <button @click="addCard()" type="button" class="addcard">
        Generate Flash Card
      </button>
    </div>
    <!-- end of add card box -->
    <span :class="{ '-show': error }" class="error"
      >Oops! Flashcards must be completed by filling the "Enter Passage" field.</span
    >
  </div>
</template>

<script>
const uuidv4 = require("uuid/v4");
const colors = ["-orange", "-red", "-purple", "-blue", "-green"];
import axios from "axios";

export default {
  name: "AddNewCard",
  data() {
    return {
      front: "",
      back: "",
      passage: "",
      error: false
    };
  },
  methods: {

    underline(word) {
      return "<u>" + word + "</u>";
    },

    getFrontBack() {
      let url = "http://localhost:5000/v1/";
      //passage = this.passage;
      // Call backend to front and back (Question and Answer)
      axios.post(url, {
        passage: this.passage
      })
      .then(function (response) {
      this.id = repsonse.date.card_id
      this.front = response.data.front;
      this.back = response.data.back;
      })
      .catch(function (error) {});
      // Example end of function
      //let summary = "A common technology for front end development is Vue.js.";
      //let keyword = "Vue.js";
      //this.front = summary.replace(keyword, "____");
      //this.back = summary.replace(keyword, this.underline(keyword));
    },

    addCard() {
      if (!this.passage) {
        this.error = true;
      } else {
        this.getFrontBack();
        const card = {
          id: this.id,
          front: this.front,
          back: this.back,
          flipped: false,
          liked: false,
          color: `${colors[Math.floor(Math.random() * colors.length)]}`,
          passage: this.passage
        };
        this.$emit("addCardTrigger", card);
        this.passage = "";
        this.front = "";
        this.back = "";
        this.error = false;
      }
    }
  }
};
</script>

<style scoped lang="sass">
@import 'src/assets/sass/_variables.sass';

.addcard-box
  margin-top: 40px
  margin-bottom: .5rem
  transition: margin-bottom .3s
  &.-showerror
    margin-bottom: 2rem
    .error
      opacity: 1
      visibility: visible
  .error
    margin-top: 15px
    display: block
    font-size: 0.8571rem
    color: red
    opacity: 0
    transition: all .5s
    visibility: hidden
    line-height: 1.4

.form-box
  display: flex
  justify-content: center
  @media (max-width: 700px)
    flex-direction: column
    align-items: center
    label
      max-width: 300px
      width: 100%
  .input, .addcard
    padding-left: 20px
    padding-right: 20px
    height: 40px
    border-width: 1px
    border-style: solid
    border-radius: $radius
    display: inline-block
    @media (max-width: 700px)
      max-width: 300px
      width: 100%
  .input
    border-color: $input-border
    font-size: 1.071rem
    color: $muted
    transition: border-color .3s
    @media (min-width: 701px)
      margin-right: 1.3rem
    @media (max-width: 700px)
      margin-bottom: 1rem
    &:hover
      border-color: darken($input-border, 20%)
    &.-error
      border-color: red
    &:not(.-error):focus
      border-color: $highlight

.addcard
  background-color: $highlight
  border-color: $highlight
  color: white
  box-shadow: 0 0 8px 1px rgba(96,69,255,0.28)
  transition: background-color .3s
  font-weight: $medium
  &:hover
    background-color: darken($highlight, 5%)
</style>
