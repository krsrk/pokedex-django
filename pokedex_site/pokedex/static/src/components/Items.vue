<template>
  <div class="max-w-xs rounded overflow-hidden shadow-lg my-5" v-for="it in dataItem" :key="it.id">
    <img loading="lazy" class="w-full" :src="it.image_url" :alt="it.name">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ it.code }} - {{ it.name }}</div>
      <p class="text-grey-darker text-base">
        <b>Height: </b> {{ it.height }} <br>
        <b>Weight: </b> {{ it.weight }} <br>
        <b>Ability: </b> {{ it.ability }}
      </p>
    </div>
    <div class="px-6 py-4">
      <a :href="it.more_info_url" target="_blank"
         class="tracking-wider text-white bg-red-500 px-4 py-1 text-sm rounded leading-loose mx-2 font-semibold"
         :title="it.name">
        <i class="fas fa-info-circle" aria-hidden="true"></i> More Info
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Items",
  props: {
    dataItem: {
      type: Array,
    },
  },
}
</script>