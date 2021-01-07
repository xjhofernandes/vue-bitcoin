<template>
  <div class="chart">
    <apexchart
      type="area"
      :options="chart.chartOptions"
      :series="chartSerie.series"
    ></apexchart>
    <div>
      <button class="button mr-1" @click="updateChart('seven')">7 D</button>
      <button class="button mr-1" @click="updateChart('month')">1 M</button>
      <button class="button mr-1" @click="updateChart('sixmonths')">6 M</button>
      <button class="button mr-1" @click="updateChart('year')">1 Y</button>
      <button class="button mr-1" @click="updateChart('max')">Max</button>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
import { reactive } from 'vue';

export default {
  name: 'HelloWorld',
  components: {
    apexchart: VueApexCharts,
  },
  setup(){
    const chart = reactive({
      chartOptions: {
        chart: {
          width: '100%',
          id: "vuechart-example",
          type: 'area',
          stacked: false,
          zoom: {
            enabled: false
          },          
        },
        colors: ["#02182B"],
        dataLabels: {
          enabled: false
        },
        markers:{
          size: 0
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [20, 100, 100, 100]            
          }
        },
        xaxis: {
          categories: [1578798000000,1581476400000,1583982000000,1586660400000,1589252400000,1591930800000,1594522800000,1597201200000],
          type: 'datetime',
          axisBorder: {
            show: false},
          axisTicks: {
            show: false},
          tooltip: {
              shared: true},
          legend: {
            position: 'top',
            horizontalAlign: 'right',
            offsetX: -10
          },        
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'BRL' }).format(value);
            },
          },
        },
      },
    });
    
    const chartSerie = reactive({
      series: [
        {
          name: "Bitcoin",
          data: [30, 40, 45, 50, 49, 60, 70, 99],
        }
      ],
    });

    async function updateChart(periodValue) {
      let valores = await requisicaoAPI(periodValue);

      let bitcointValues = valores.map(function(valor) {return valor['closing']});
      let bitCoinDate = valores.map(function(valor) {return valor['date'].$date});

      const colors = ["#02182B"]; 

      chart.chartOptions = {
        colors: [colors[Math.floor(Math.random() * colors.length)]],
        xaxis:{
          categories : bitCoinDate
        }
      };
    
      chartSerie.series = [
        {
          data: bitcointValues,
        },
      ];
    }

    async function requisicaoAPI(periodValue) {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        body: JSON.stringify({ period: periodValue})
      };

      let data = await fetch("https://vue-bitcoin.herokuapp.com/updateChart", requestOptions)
        .then((response) => response.json())
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error(error);
        });
      return JSON.parse(data);
    }
    
    return {updateChart, chart, chartSerie, requisicaoAPI}
  },
  mounted(){
    this.updateChart('month');
  }
}
</script>

<style lang="scss">

</style>
