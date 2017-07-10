<template lang="jade">
.room
  h2 Welcome to room \#{{ $route.params.label }}
  chat-room.chatroom
</template>

<script>
import ChatRoom from '@/components/ChatRoom';

export default {
  data() {
    return {
      label: '',
    };
  },
  mounted() {
  },
  methods: {},
  components: {
    ChatRoom,
  },
};
</script>

<style lang="stylus" scoped>
.chatroom
  margin-left auto
  margin-right auto
</style>
