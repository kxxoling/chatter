<template lang="jade">
.chatroom
  .msgs
    h3.tips(v-if="!messages.length") Welcome! Be the 1st to say something!
    .msg(
      v-for="o in messages",
      v-bind:class="{ 'current-user': o.username==currentUser }"
    )
      img.avatar(v-bind:src="o.avatar", alt="o.username")
      .text
        .sender
          span.name {{ o.name }}
          span.time {{ moment(o.timestamp) }}
        p {{ o.message }}
  .msg-sender
    input.input(
      v-model="input",
      @keyup.enter="submit",
      placeholder="Write a message...")
    button.submit Send
</template>

<script>
import moment from 'moment';
import axios from 'axios';

export default {
  data() {
    return {
      ws: null,
      status: 'not initialised',
      input: '',
      messages: [],
    };
  },
  computed: {
    currentUser() {
      return 'kxxoling';
    },
  },
  mounted() {
    this.initWs();
  },
  methods: {
    initWs() {
      this.loadMsgs();
      const wsScheme = window.location.protocol === 'https:' ? 'wss' : 'ws';
      const roomLabel = this.$route.params.label;
      const ws = new WebSocket(`${wsScheme}://${window.location.hostname}:8000/chat/${roomLabel}`);
      ws.onmessage = this.rcvMsg;
      this.ws = ws;
    },
    loadMsgs() {
      axios.get(`/api/room/${this.$route.params.label}`)
      .then((rsp) => {
        this.messages = rsp.data.messages;
      });
    },
    submit() {
      const message = this.input;
      this.input = '';
      this.ws.send(JSON.stringify({ message }));
    },
    rcvMsg(msg) {
      const data = JSON.parse(msg.data);
      this.messages.push(data);
    },
    moment() {
      return moment().format('YYYY MMMM Do, h:mm:ss');
    },
  },
};
</script>

<style lang="stylus" scoped>
.chatroom
  width 40rem
  border 1px solid green

  .msgs
    padding 1rem
    height 40rem
    overflow auto

  .msg
    display flex
    flex-direction row-reverse
    align-items flex-start
    width 100%
    margin-bottom 1rem
    &:last-child
      margin-bottom 0

    .avatar
      border-radius 50%
      height 4rem
      margin-left 1rem
      margin-bottom 1rem

    .sender
      margin-bottom 0.6rem
      display flex
      justify-content space-between

      .name
        color blue
      .time
        color #777

    .text
      background-color #eee
      border-radius 4px
      width 100%
      padding 0.6rem

      p
        margin 0

  .msg.current-user
    flex-direction row
    .avatar
      margin-left 0
      margin-right 1rem

  .msg-sender
    width 100%
    display flex
    height 2.6rem

    .input
      padding 0 0.6rem
      flex 1

    .submit
      background-color #44e
      color white
      border none
      padding 0 1rem
</style>
