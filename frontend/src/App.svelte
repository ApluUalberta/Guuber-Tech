<script lang="ts">
  import FeedbackList from "./components/FeedbackList.svelte";
  import FeedbackStats from "./components/FeedbackStats.svelte";
  import FeedbackForm from "./components/FeedbackForm.svelte";

  let feedback = [
    {
      id: 1,
      rating: 10,
      text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eu est in turpis egestas cursus id ac purus. Sed malesuada tortor quis efficitur porttitor. Suspendisse dapibus, tellus sit amet viverra placerat, justo nulla vulputate diam, at accumsan tortor eros nec neque. Praesent nisi risus, fermentum eu placerat eu, elementum vitae sapien.",
    },
    {
      id: 2,
      rating: 9,
      text: "Ut tristique lorem ut lacus suscipit, et malesuada nisi fermentum. Sed condimentum placerat ipsum at molestie. Pellentesque eros purus, accumsan id tincidunt quis, bibendum a orci. Donec et leo eu quam suscipit lobortis ut vel mi.",
    },
    {
      id: 3,
      rating: 8,
      text: "Morbi vel dictum purus. Vestibulum dignissim viverra tellus quis ultricies. Aenean non mauris id massa efficitur finibus sed facilisis massa. Ut tempor odio et condimentum ornare. Morbi luctus cursus sapien, a auctor justo dignissim ut. Duis scelerisque sodales leo, aliquet vestibulum metus pharetra ut. Duis tincidunt, odio sit amet varius maximus, dolor sem vehicula enim, vitae ullamcorper odio metus non nibh.",
    },
  ];

  const deleteFeedback = (e) => {
    let itemId: number = e.detail;
    feedback = feedback.filter((item) => item.id !== itemId);
  };

  const addFeedback = (e) => {
	let newFeedback = e.detail;
	feedback = [newFeedback, ...feedback]
  }

  $: count = feedback.length;
  $: average = feedback.reduce((a, { rating }) => a + rating, 0) / count;
</script>

<main class="container">
  <FeedbackForm on:add-feedback={addFeedback} />
  <FeedbackStats {count} {average} />
  <FeedbackList {feedback} on:delete-feeback={deleteFeedback} />
</main>
