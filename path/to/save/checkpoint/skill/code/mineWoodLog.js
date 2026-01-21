async function mineWoodLog(bot) {
  // Step 1: Explore until we find a wood log
  const woodLog = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const log = bot.findBlock({
      matching: block => block.name.endsWith('_log'),
      // Check for any type of log
      maxDistance: 32
    });
    return log;
  });

  // Step 2: If we found a log, mine it
  if (woodLog) {
    bot.chat("Found a wood log, mining it now.");
    await mineBlock(bot, woodLog.name, 1);
    bot.chat("Successfully mined a wood log.");
  } else {
    bot.chat("No wood log found within the time limit.");
  }
}