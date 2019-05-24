<template>
  <div >
   <img :src="imageUrl" alt="image" width="350" height="350">
  </div>
</template>

<script>
import { ipcRenderer } from 'electron';

export default {
  created() {
    ipcRenderer.on('image', (event, arg) => {
      this.imageUrl = arg
    })
  },
  data() {
    return {
      imageUrl: ''
    }
  }
}
</script>