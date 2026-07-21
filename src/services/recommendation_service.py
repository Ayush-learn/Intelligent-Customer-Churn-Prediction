def get_recommendations(probability, customer):
    """
    Generate business recommendations based on churn probability
    and customer information.
    """

    recommendations = []

    if probability >= 0.70:

        recommendations.append("📞 Contact the customer within 48 hours.")
        recommendations.append("🎁 Offer a loyalty discount.")
        recommendations.append("👨‍💼 Assign a retention executive.")

    elif probability >= 0.30:

        recommendations.append("📧 Send a personalized retention email.")
        recommendations.append("💳 Recommend a yearly contract.")
        recommendations.append("🎉 Offer promotional benefits.")

    else:

        recommendations.append("😊 Continue regular engagement.")
        recommendations.append("🏆 Reward customer loyalty.")

    # Personalized recommendations
    if customer["Contract"] == "Month-to-month":
        recommendations.append("📅 Recommend switching to a longer-term contract.")

    if customer["TechSupport"] == "No":
        recommendations.append("🛠 Offer a Tech Support add-on.")

    if customer["OnlineSecurity"] == "No":
        recommendations.append("🔒 Promote the Online Security service.")

    return recommendations